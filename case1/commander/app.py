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
        general1_result = ""
        general2_result = ""
        general3_result = ""
        try:
            general1_result = requests.get("http://172.30.48.1:5051/general1_result")
            general2_result = requests.get("http://172.30.48.1:5052/general2_result")
            general3_result = requests.get("http://172.30.48.1:5053/general3_result")

        except requests.exceptions.RequestException as e:
            return "error"

        # n >= 3*f + 1 계산
        n = 3
        f = 0

        list = [general1_result.text, general2_result.text, general3_result.text]
        new_list = []
        for v in list:
            if v not in new_list:
                new_list.append(v)

        cnt_one = list.count(new_list[0])
        cnt_two = list.count(new_list[1])

        if(cnt_one < cnt_two):
            f = cnt_one
        else:
            f = cnt_two

        result = ""
        if(n >= (3*f) + 1):
            result = "합의 가능"
        else:
            result = "합의 불가능"


        # 출력 만들기
        general1 = "< general1:" + general1_result.text + " >"
        general2 = "< general2:" + general2_result.text + " >"
        general3 = "< general3:" + general3_result.text + " >"

        RESULT = general1 + " " + general2 + " " + general3 + " " + result

        return RESULT

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5000, debug = True)