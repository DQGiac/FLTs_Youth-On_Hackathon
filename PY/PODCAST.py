from PIL import Image
import pytesseract
import os
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import ffmpeg

def ocr(image_src):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
    text = pytesseract.image_to_string(image_src, lang="vie")
    return text

def speak(text):
    # print("Bot: {}".format(text))
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.wav")
    song = AudioSegment.from_file("sound.wav")
    play(song)

t = "0"
while t != "1" and t != "2":
    t = input("Bạn muốn lấy dữ liệu từ ảnh hay từ văn bản? Nhập 1 có nghĩa là ảnh, 2 có nghĩa là văn bản: ")
if t == "1":
    filename = input("Nhập tên file: ")
    user_message = ocr(filename)
    print("Đang thiết lập giọng nói ảo...")
else:
    print("Nhấn enter để xuống dòng, nhấn enter lần nữa để kết thúc nhập.\nNếu paste, hãy chắc chắn không có đoạn nào cách nào quá hai dòng.")
    content = ""
    user_message = ""
    while True:
        t = input()
        if t == "":
            print("Đang thiết lập giọng nói ảo...")
            break
        else:
            user_message += t + "\n"

# print(user_message)
speak(user_message)