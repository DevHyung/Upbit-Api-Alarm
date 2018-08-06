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
    print("[ {} ] by API : 코인 심볼 수집".format(get_time_str()))
    KRW_List = []
    BTC_List = []
    ETH_List = []
    USDT_List = []
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    jsonStr = json.loads(response.text)
    for coin in jsonStr:
        if 'BTC-' in coin['market']:
            BTC_List.append(coin['market'].strip())
        elif 'KRW-' in coin['market']:
            KRW_List.append(coin['market'].strip())
        elif 'ETH-' in coin['market']:
            ETH_List.append(coin['market'].strip())
        else:
            USDT_List.append(coin['market'].strip())

    print("[ {} ] by API : 코인 심볼 수집 완료".format(get_time_str()))

    # === 감지부분

    print("[ {} ] by API : 상장 감시중...".format(get_time_str()))
    idx = 1
    while True:
        if idx % 1000 == 0:
            print("[ {} ] by API : {}회 모니터링중...".format(get_time_str(),idx))
        try:
            url = "https://api.upbit.com/v1/market/all"
            response = requests.request("GET", url)
            jsonStr = json.loads(response.text)
            for coin in jsonStr:
                if 'BTC-' in coin['market']:
                    if coin['market'] not in BTC_List:
                        print("* [ {} ] by API : {} 코인 상장 감지".format(get_time_str(),coin['market']))
                        play_alarm()
                        BTC_List.append(coin['market'].strip())
                elif 'KRW-' in coin['market']:
                    if coin['market'] not in KRW_List:
                        print("* [ {} ] by API : {} 코인 상장 감지".format(get_time_str(), coin['market']))
                        play_alarm()
                        KRW_List.append(coin['market'].strip())

                elif 'ETH-' in coin['market']:
                    if coin['market'] not in ETH_List:
                        print("* [ {} ] by API : {} 코인 상장 감지".format(get_time_str(), coin['market']))
                        play_alarm()
                        ETH_List.append(coin['market'].strip())
                else:
                    if coin['market'] not in USDT_List:
                        print("* [ {} ] by API : {} 코인 상장 감지".format(get_time_str(), coin['market']))
                        play_alarm()
                        USDT_List.append(coin['market'].strip())
        except:
            print("[ {} ] by API : Upbit API 호출에러 프로그램 확인바람".format(get_time_str()))
        time.sleep(delay)
        idx+=1


