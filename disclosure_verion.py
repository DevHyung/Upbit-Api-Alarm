# 공시버전
import requests
import json
import time
from pygame import mixer
mixer.init()
def get_time_str():
    now = time.localtime()
    nowTime = "%04d-%02d-%02d %02d:%02d:%02d" % (
    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return nowTime

def play_alarm():
    mixer.music.load('./alarm.mp3')
    mixer.music.play()

if __name__ == "__main__":

    # === CONFIG
    delay = float(input("검사 주기를 입력하세요(초 단위) :: "))
    print("알람 소리확인 ( 방금 들린 소리가 상장시 재생됩니다. )")
    play_alarm()

    # === 초기화 부분
    html = requests.get('https://project-team.upbit.com/api/v1/disclosure?region=kr&per_page=20')
    jsonStr = json.loads(html.text)
    dataDict = {}
    for data in jsonStr['data']['posts']:
        dataDict[data['id']] = "[{}] {}".format(data['assets'], data['text'])

    # === 감지부분

    print("[ {} ] : 프로젝트 공시 감시 시작...".format(get_time_str()))
    idx = 1
    while True:
        if idx % 1000 == 0:
            print("[ {} ] : {}회 모니터링중...".format(get_time_str(),idx))
        try:
            html = requests.get('https://project-team.upbit.com/api/v1/disclosure?region=kr&per_page=20')
            jsonStr = json.loads(html.text)
            for data in jsonStr['data']['posts']:
                if data['id'] in dataDict:
                    pass
                else:
                    dataDict[data['id']] = "[{}] {}".format(data['assets'], data['text'])
                    print("\t>>> 새공지 [ {} ] : {} ".format(get_time_str(), dataDict[data['id']]))
                    play_alarm()
        except:

            print("[ {} ] by API : Upbit API 호출에러 프로그램 확인바람".format(get_time_str()))
        time.sleep(delay)
        idx+=1


