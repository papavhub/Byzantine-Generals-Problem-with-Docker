from flask import Flask
app = Flask(__name__)
import requests

### BYZANTINE ###
container_name = "<General2:최혜민>"

@app.route('/')
def general2_service():
	return container_name

@app.route('/commander') # 메시지 전달
def get_general2():
        commander_response = ""
        try:
            commander_response = requests.get("http://172.31.208.1:5050/commander")
            print(commander_response)
        except requests.exceptions.RequestException as e:
            return "error"
        return "홍길동"

@app.route('/general2_result') # 합의 결과 통보
def general2_result():
        commander_response = ""
        command = ""
        try:
            general1_response = requests.get("http://172.31.208.1:5051/commander")
            general3_response = requests.get("http://172.31.208.1:5053/commander")

            if(general1_response == general3_response):
                command = "합의 가능"
            else:
                command = "합의 불가능"

        except requests.exceptions.RequestException as e:
            return "error"

        return command


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5002, debug = True)