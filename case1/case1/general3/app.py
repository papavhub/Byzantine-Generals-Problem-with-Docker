from flask import Flask
app = Flask(__name__)
import requests

container_name = "<General3:최혜민>"

@app.route('/')
def general2_service():
	return container_name

@app.route('/commander') # 메시지 전달
def get_general3():
        commander_response = ""
        try:
            commander_response = requests.get("http://172.31.208.1:5050/commander")
            print(commander_response)
        except requests.exceptions.RequestException as e:
            return "error"
        return commander_response.text

@app.route('/general3_result') # 합의 결과 통보
def general3_result():
        commander_response = ""
        command = ""
        try:
            general2_response = requests.get("http://172.31.208.1:5052/commander")
            general3_response = requests.get("http://172.31.208.1:5053/commander")

            if(general2_response == general3_response):
                command = "합의 가능"
            else:
                command = "합의 불가능"

        except requests.exceptions.RequestException as e:
            return "error"

        return command


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5003, debug = True)