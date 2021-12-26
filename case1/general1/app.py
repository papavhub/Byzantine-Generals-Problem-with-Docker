from flask import Flask
app = Flask(__name__)
import requests

container_name = "general1"

@app.route('/')
def general1_service():
	return container_name

@app.route('/general1_result') # 메시지 받기
def get_general1():
        commander_response = ""
        try:
            commander_response = requests.get("http://commander_con:5000/commander")
        except requests.exceptions.RequestException as e:
            return "error"
        return commander_response.text


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)