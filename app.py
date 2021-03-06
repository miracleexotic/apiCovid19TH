from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import time

app = Flask(__name__)

def getDetail():
    url = 'https://ddc.moph.go.th/viralpneumonia/eng/index.php'
    res = requests.get(url)
    res.encoding = "utf-8"
    print(res)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    day = soup.find_all("div", {"class": "w3-padding mybg3 w3-round-large"})
    resultDay = { "DayfromWeb" : str(day[0]).split('">')[1][:-6], "TimefromWeb" : str(day[1]).split('">At ')[1][:-6] }
    # print(resultDay)
    totalCase = soup.find_all("div", {"class": "header_blog mybg2"})
    result_total = { "total" : str(totalCase).split('">')[2][:-12] }
    # print(result_total)
    newCase = soup.find_all("div", {"class": "mybg1"})
    result_new = { "New" : str(newCase).split(", ")[0].split('">')[2][:-11] }
    # print(result_new)
    seriousCase = soup.find_all("div", {"class": "mybg2"})
    result_serious = { "Serious" : str(seriousCase[1]).split('">')[2][:-11] }
    # print(result_serious)
    deathsCase = soup.find_all("div", {"class": "mybg3"})
    result_deaths = { "Deaths" : str(deathsCase[2]).split('">')[2][:-11] }
    # print(result_deaths)

    lst_time = time.gmtime(time.time() + 25200)
    currentTime = { "currentTime" : time.strftime("%d %b %Y %H:%M:%S", lst_time) }
    # print([{**resultDay, **result_total, **result_new, **result_serious, **result_deaths}]
    return [{**resultDay, **result_total, **result_new, **result_serious, **result_deaths, **currentTime}]

@app.route('/')
def index():
  return "api use for mission \n[built from web scarping] >>> /api/covid19-TH"

@app.route('/api/covid19-TH', methods=['GET'])
def get_api():
    return jsonify(getDetail()), 200


if __name__ == "__main__":
    app.run(debug=True)
    # getDetail()




