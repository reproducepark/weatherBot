import xml.etree.ElementTree as ET
import requests, os
from dotenv import load_dotenv


def getWeather():
    url = os.environ.get('weatherUrl')
    response = requests.get(url)
    res = []

    if response.status_code == 200:
        xml_content = response.content

        tree = ET.ElementTree(ET.fromstring(xml_content))
        root = tree.getroot()

        for data in root.findall('.//data'):
            hour = data.find('hour').text
            temp = data.find('temp').text
            wfKor = data.find('wfKor').text
            pop = data.find('pop').text
            res.append([hour, temp, wfKor, pop])

    return res
    
def makeMsg():
    res = getWeather()
    emoDict = {"맑음":"☀️","구름 많음":"☁","흐림":"☁","비":"☔","비/눈":"☔","눈":"❄️","소나기":"☂"}

    msg =""
    for idx in range(4):
        hour, temp, wfKor, pop = res[idx]
        msg += f"{hour}시 기온 : {temp}°C, 날씨 : {wfKor}{emoDict[wfKor]}, 강수확률 : {pop}%\n"

    return msg[:-1]

if __name__ == "__main__":
    print(makeMsg())