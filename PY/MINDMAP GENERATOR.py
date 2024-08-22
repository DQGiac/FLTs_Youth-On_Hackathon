import skimage
from PIL import Image
import numpy as np
import io
from graphviz import Source
import google.generativeai as genai
import cv2
import pytesseract

def gemini(user_message):
    # def chatGPT(ques):
    #     url = "https://chatgpt-api8.p.rapidapi.com/"
    #     payload = [
    #         {
    #             "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
    #             "role": "system"
    #         },
    #         {
    #             "content": f"{ques}",
    #             "role": "user"
    #         }
    #     ]
    #     headers = {
    #         "content-type": "application/json",
    #         "X-RapidAPI-Key": "d89a8977f9mshd28e97843a01cf2p158370jsn0cb69019b238",
    #         "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    #     }
    #     # huytrongnghia: 8dd3bfa3f3mshda3845149bb330ep1c4505jsna147eee499b5
    #     # khkt: d89a8977f9mshd28e97843a01cf2p158370jsn0cb69019b238
    #     # huynghia: 8eacc0c16dmshb79a0fe65bc3344p14e02ajsn29bf84e2e8b9
    #     # huytrong: 030c80dc47mshbe06ccceee3100cp18b554jsnc6867b4f1b65
    #     # nguyenquynh: 0c6c1ec218msh58fce662b00a268p1e2172jsn77027176568f
    #     response = requests.post(url, json=payload, headers=headers)
    #     data = response.json()
    #     return data["text"]


    def gemini(ques):
        genai.configure(api_key="AIzaSyCfM6NvU3tQ_pr7gepDw02PYVTwIR6GjOM")
        model = genai.GenerativeModel('gemini-1.5-pro')
        a = (model.generate_content(ques))
        return a.candidates[0].content.parts[0].text


    bot_message = gemini("Hãy rút gọn thông tin và tạo code DOT biễu diễn nội dung của đoạn văn sau:\n" + user_message)
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
        temp_img = './static/mindmap'
        s.format = 'png'
        s.render(temp_img)
        return ["./static/mindmap.png", "Đây là hình ảnh mindmap được tạo bởi AI, có thể có một số sai sót.\nNếu không như mong muốn, bạn hãy ghi thêm các ý bạn muốn vào prompt như sau:\nChiến dịch Điện Biên Phủ --> Chiến dịch Điện Biên Phủ - diễn biến và kết quả"]
    except Exception as e:
        return ["./static/error.png", "Đã xảy ra một số lỗi, có thể do prompt hoặc do AI\n" + str(e)]

def ocr(image_src):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
    text = pytesseract.image_to_string(image_src, lang="vie")
    return text

t = 0
while t != "1" and t != "2":
    t = input("Bạn muốn lấy dữ liệu từ ảnh hay từ văn bản? Nhập 1 có nghĩa là ảnh, 2 có nghĩa là văn bản: ")
if t == "1":
    user_message = ocr("./static/test.png")
else:
    print("Nhấn enter để xuống dòng, nhấn enter lần nữa để kết thúc nhập.\nNếu paste, hãy chắc chắn không có đoạn nào cách nào quá hai dòng.")
    content = ""
    user_message = ""
    while True:
        t = input()
        if t == "":
            break
        else:
            user_message += t + "\n"

print("Đang tạo code...")
a = gemini(user_message)
print("Đang tạo mindmap...\n")
cv2.imshow("Mindmap", cv2.imread(a[0]))
print(a[1])
if cv2.waitKey(0):
    cv2.destroyAllWindows()