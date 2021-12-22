from flask import Flask
app = Flask(__name__)
import requests

container_name = "general3"

@app.route('/')
def general2_service():
	return container_name

@app.route('/general3_result') # 메시지 받기
def get_general3():
        commander_response = ""
        try:
            commander_response = requests.get("http://172.30.48.1:5050/commander")
        except requests.exceptions.RequestException as e:
            return "error"
        return commander_response.text

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5003, debug = True)