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
def get_symbol_list():
    print("[ {} ] >>> : 코인 심볼 초기화".format(get_time_str()))
    KRW_List = []
    BTC_List = []
    ETH_List = []
    USDT_List = []
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    jsonStr = json.loads(response.text)
    for coin in jsonStr:
        if 'BTC-' in coin['market']:
            KRW_List.append(coin['market']+'\n')
        elif 'KRW-' in coin['market']:
            BTC_List.append(coin['market']+'\n')
        elif 'ETH-' in coin['market']:
            ETH_List.append(coin['market']+'\n')
        else:
            USDT_List.append(coin['market']+'\n')

    print("[ {} ] >>> : 코인 심볼 초기화 완료".format(get_time_str()))

def valid_user():
    # 20180806 17:10기준 20시간
    #print(time.time())
    now = 1533542992.9937532
    terminTime = now + 60 * 60 * 20
    print("체험판 만료기간 : ", time.ctime(terminTime))
    if time.time() > terminTime:
        print('만료되었습니다.')
        exit(-1)
    else:
        print(">>> 프로그램이 실행되었습니다.")


if __name__ == "__main__":
    valid_user()
    get_symbol_list()