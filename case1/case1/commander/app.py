from flask import Flask
app = Flask(__name__)
import requests

container_name = "Commaner"
start_command = "최혜민"

@app.route('/')
def commander_service():
	return "COMMANDER"

@app.route('/commander')
def commander_start():
        return start_command

@app.route('/final_result')
def final_result():
        try:
            genera1_result = requests.get("http://172.31.208.1:5051/general1_result")
            genera2_result = requests.get("http://172.31.208.1:5052/general2_result")
            genera3_result = requests.get("http://172.31.208.1:5053/general3_result")
        except requests.exceptions.RequestException as e:
            return "error"

        result = "< beeb389849f0:최혜민 > : " + genera1_result.text + "<br>" +  "< e5ca46c24eae:최혜민 > : " + genera2_result.text +  "<br>" +  "< 65b084d6ab6c:최혜민 > : " + genera3_result.text
        return result

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5000, debug = True)