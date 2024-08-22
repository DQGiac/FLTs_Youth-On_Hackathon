import requests
from deep_translator import GoogleTranslator
from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route("/askGPT", methods=['POST'])
def textoimage():
	translator = GoogleTranslator(source='vi', target='en')
	a = (translator.translate(request.json["message"]))

	url = "https://open-ai21.p.rapidapi.com/texttoimage2"

	payload = { "text": a }
	headers = {
		"x-rapidapi-key": "8eacc0c16dmshb79a0fe65bc3344p14e02ajsn29bf84e2e8b9", #backup code: d89a8977f9mshd28e97843a01cf2p158370jsn0cb69019b238
		"x-rapidapi-host": "open-ai21.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers)
	return response.json()

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)