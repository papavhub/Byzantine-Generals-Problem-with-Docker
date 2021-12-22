from flask import Flask
app = Flask(__name__)
import requests

### BYZANTINE ###
container_name = "general2"

@app.route('/')
def general2_service():
	return container_name

@app.route('/general2_result') # 메시지 받기
def get_general2():
        commander_response = ""
        try:
            commander_response = requests.get("http://172.30.48.1:5050/commander")
        except requests.exceptions.RequestException as e:
            return "error"
        return "홍길동"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5002, debug = True)