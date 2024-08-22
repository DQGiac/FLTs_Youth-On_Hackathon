import google.generativeai as genai
def gemini(ques):
    genai.configure(api_key="AIzaSyCfM6NvU3tQ_pr7gepDw02PYVTwIR6GjOM")
    model = genai.GenerativeModel('gemini-1.5-flash')
    a = (model.generate_content(ques))
    return a.candidates[0].content.parts[0].text

# print(gemini("Bạn hãy dịch ra tiếng anh và output 1 câu duy nhất từ câu văn sau:\nHết sức đánh từ giờ mão đến giờ dậu, Tiếp bị thương, rớt xuống nước, giặc móc lên bắt, dùng thuốc độc giết."))
import requests
def texttoimage():
    url = "https://open-ai21.p.rapidapi.com/texttoimage2"
    payload = { "text": "Asia:" + "He was continuously attacked from dawn till noon, wounded, fell into the water, captured by the enemy, and poisoned to death." }
    headers = {
    	"x-rapidapi-key": "8eacc0c16dmshb79a0fe65bc3344p14e02ajsn29bf84e2e8b9",
    	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
    	"Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    return response.json()["generated_image"]
print(texttoimage())