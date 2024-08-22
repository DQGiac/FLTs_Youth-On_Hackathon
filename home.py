from flask import Flask, render_template, request, send_file, jsonify
import skimage
from PIL import Image
import numpy as np
import io
import json
import requests
from graphviz import Source
import google.generativeai as genai
import pytesseract
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS

app = Flask(__name__)


@app.route("/")
def home(): return render_template('home.html')

@app.route("/home")
def home1(): return render_template('home.html')

@app.route("/mindmap")
def mindmap(): return render_template('mindmap.html')

@app.route("/strtell")
def strtell(): return render_template('strtell.html')

@app.route("/podcast")
def podcast(): return render_template('podcast.html')

@app.route('/save-image', methods=['POST'])
def save_image():
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename != '':
            image_file.save(f'./static/ocr.png')
            return jsonify({'filename': image_file.filename})
    return jsonify({'error': 'No image uploaded'})

@app.route("/ocr", methods=["POST"])
def ocr():
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
    text = pytesseract.image_to_string(Image.open("./static/ocr.png"), lang="vie")
    return jsonify({"message": text})

@app.route("/mindmap_gen", methods=['POST'])
def mindmap_gen():
    def gemini(ques):
        genai.configure(api_key="AIzaSyCfM6NvU3tQ_pr7gepDw02PYVTwIR6GjOM")
        model = genai.GenerativeModel('gemini-1.5-pro')
        a = (model.generate_content("" + ques))
        return a.candidates[0].content.parts[0].text

    data = request.get_json()
    user_message = data['message']

    # Call your ChatGPT function here
    bot_message = gemini('Hãy rút gọn thông tin và tạo code DOT (shape=box, style=filled, fillcolor=black, fontcolor=white) biễu diễn nội dung của đoạn văn sau:\n' + user_message)
    # return jsonify({"content": bot_message})

    bot_message_dot = bot_message
    open_paren = -1
    for i in range(len(bot_message)):
        if bot_message[i:i + 5] == "graph":
            for j in range(i + 5, len(bot_message)):
                if bot_message[j] == "{":
                    open_paren += 1
                    if open_paren == 0:
                        open_paren += 1
                if bot_message[j] == "}":
                    open_paren -= 1
                if open_paren == 0:
                    bot_message_dot = bot_message[i : j + 1]
                    break
            break
        if bot_message[i:i + 7] == "digraph":
            for j in range(i + 7, len(bot_message)):
                if bot_message[j] == "{":
                    open_paren += 1
                    if open_paren == 0:
                        open_paren += 1
                if bot_message[j] == "}":
                    open_paren -= 1
                if open_paren == 0:
                    bot_message_dot = bot_message[i : j + 1]
                    break
            break
    try:
        s = Source(bot_message_dot, format="png")
        temp_img = './static/mindmap' + str(data['mindmapind'])
        s.format = 'png'
        s.render(temp_img)
        return jsonify({ 'content': "Đây là hình ảnh mindmap được tạo bởi AI, có thể có một số sai sót.\nNếu không như mong muốn, bạn hãy ghi thêm các ý bạn muốn vào prompt như sau:\n<i>Chiến dịch Điện Biên Phủ</i> --> <i>Chiến dịch Điện Biên Phủ - diễn biến và kết quả</i>" })
    except Exception as e:
        s = Image.open("./static/error.png")
        s.save("./static/mindmap" + str(data["mindmapind"]) + ".png")
        return jsonify({ "content": str(e) })

@app.route("/podcast_gen", methods=['POST'])
def podcast_gen():
    tts = gTTS(text=request.json["message"], lang="vi", slow=False)
    tts.save("sound.wav")
    # song = AudioSegment.from_file("sound.wav")
    # play(song)

@app.route("/strtell_gen", methods=['POST'])
def strtell_gen():
    tts = gTTS(text=request.json["message"], lang="vi", slow=False)
    tts.save("sound.wav")
    song = AudioSegment.from_file("sound.wav")
    play(song)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)