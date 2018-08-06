import requests
import json
import time
from openpyxl import Workbook
#===    GLOBAL
excelHeader = ['코인명','현재가','전일대비','거래대금']
FILENAME = 'coin.xlsx'
def get_symbol_list():
    print(">>> 코인 심볼 받아오기 시작 ")
    KRW_File = open("KRW_LIST.txt",'w')
    BTC_File = open("BTC_LIST.txt",'w')
    ETH_File = open("ETH_LIST.txt",'w')
    USDT_File = open("USDT_LIST.txt",'w')
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    jsonStr = json.loads(response.text)
    for coin in jsonStr:
        if 'BTC-' in coin['market']:
            BTC_File.write(coin['market']+'\n')
        elif 'KRW-' in coin['market']:
            KRW_File.write(coin['market']+'\n')
        elif 'ETH-' in coin['market']:
            ETH_File.write(coin['market']+'\n')
        else:
            USDT_File.write(coin['market']+'\n')
    USDT_File.close()
    BTC_File.close()
    ETH_File.close()
    USDT_File.close()
    print(">>> 코인 심볼 받아오기 끝 ")

def valid_user():
    # 20180806 17:10기준 20시간
    print(time.time())
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