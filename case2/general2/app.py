from flask import Flask
app = Flask(__name__)
import requests

container_name = "<General2:최혜민>"

@app.route('/')
def general2_service():
	return container_name

@app.route('/general2_result') # 메시지 전달
def get_general2():
        commander_response = ""
        try:
            commander_response = requests.get("http://commander_con:5000/commander")
        except requests.exceptions.RequestException as e:
            return "error"
        return commander_response.text


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5002, debug = True)