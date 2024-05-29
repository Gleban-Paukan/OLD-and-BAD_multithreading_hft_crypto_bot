import grequests
import requests
from itertools import product
import hashlib
import hmac
import time
import coin_base

from spot.v3 import mexc_spot_v3
import hmac
import hashlib

import requests

apiKey = 'PQNjUWIFy6Jw2kG5YCL7dcKUSaTOSfVOT0K8dw1Og0UoY2R9rojQbNGovX5nYzZU'
secretKey = 'l0wOfYIRaLSZegxWbkZmLaxb0KUpVpbFYvPcgZaPKZRTZYc77lDnJYVUMwkWTSjj'

hosts = "https://api.mexc.com"
mexc_key = "mx0vglMrBYuh5ZIhjv"
mexc_secret = "bbc4e2292a864fbe84cc0b51a28a1cb5"
capital = mexc_spot_v3.mexc_capital(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
response_mexc = capital.get_coinlist()
Kucoin_base = [i["baseCurrency"] for i in requests.get('https://api.kucoin.com/api/v1/symbols').json()['data'] if
               i['quoteCurrency'] == 'USDT' and '3L' != i['baseCurrency'][
                                                        len(i['baseCurrency']) - 2: len(i['baseCurrency'])] and '3S' !=
               i['baseCurrency'][len(i['baseCurrency']) - 2: len(i['baseCurrency'])]]
response_kucoin = {}
Kucoin_response_base = [f'https://api.kucoin.com/api/v2/currencies/{i}' for i in Kucoin_base]
response = (grequests.get(url) for url in Kucoin_response_base)
timestamp = t = requests.get(
    f'https://api4.binance.com/api/v3/time',
    headers={'X-MBX-APIKEY': apiKey}).json()['serverTime']
content = f'timestamp={timestamp}'
signature = hmac.new(secretKey.encode(), content.encode(), hashlib.sha256).hexdigest()
response_binance = requests.get(
    f'https://api.binance.com/sapi/v1/capital/config/getall?{content}&signature={signature}',
    headers={'X-MBX-APIKEY': apiKey}).json()
for c, i in enumerate(grequests.map(response)):
    try:
        response_kucoin[Kucoin_base[c]] = i.json()['data']['chains']
    except:
        pass

response_bitget = requests.get(f'https://api.bitget.com/api/spot/v1/public/currencies').json()['data']
response_huobi = requests.get('https://api.huobi.pro/v2/reference/currencies').json()['data']


def mexc(Coin, response):
    for i in response:
        try:
            if i['coin'] == Coin:
                return [[w['network'], float(w["withdrawFee"]),
                         {'isWithdrawEnabled': w['depositEnable'], 'isDepositEnabled': w['withdrawEnable']}] for w in
                        i['networkList']]
        except Exception as er:
            print(i, 'qwe')


def binance(Coin, response):
    for i in response:
        try:
            if i['coin'] == Coin:
                return [[w['network'], float(w['withdrawFee']),
                         {'isWithdrawEnabled': w['withdrawEnable'], 'isDepositEnabled': w['withdrawEnable']}] for w in
                        i['networkList']]
        except Exception as er:
            print('123', i)


def kucoin(Coin, response):
    return [[i['chainName'], float(i['withdrawalMinFee']),
             {'isWithdrawEnabled': i['isWithdrawEnabled'], 'isDepositEnabled': i['isDepositEnabled']}] for i in
            response[Coin]]


def bitget(Coin, response):
    for i in response:
        if i['coinName'] == Coin:
            return [[w['chain'], float(w['withdrawFee']),
                     {'isWithdrawEnabled': w['withdrawable'], 'isDepositEnabled': w['rechargeable']}] for w in
                    i['chains']]


def gateio(Coin):
    a = []
    fees = coin_base.gateio_fees(Coin)
    for i in fees:
        a.append([i, fees[i], {'isWithdrawEnabled': True, 'isDepositEnabled': True}])
    return a


def Huobi(Coin, response):
    Coin = Coin.lower()
    for i in response:
        if i['currency'] == Coin:
            a = []
            for w in i['chains']:
                if w['withdrawStatus'] == 'allowed':
                    isWithdraw = True
                else:
                    isWithdraw = False
                if w['depositStatus'] == 'allowed':
                    isDep = True
                else:
                    isDep = False
                a.append([w['displayName'], float(w['transactFeeWithdraw']),
                          {'isWithdrawEnabled': isWithdraw, 'isDepositEnabled': isDep}])
            return a


def getNetwork(Buy_name, Sell_name, Coin):
    if Buy_name == 'Mexc':
        BN = mexc(Coin, response_mexc)
    elif Buy_name == 'Kucoin':
        BN = kucoin(Coin, response_kucoin)
    elif Buy_name == 'Bitget':
        BN = bitget(Coin, response_bitget)
    elif Buy_name == 'Gateio':
        BN = gateio(Coin)
    elif Buy_name == 'Binance':
        BN = binance(Coin, response_binance)
    else:
        BN = Huobi(Coin, response_huobi)
    if Sell_name == 'Mexc':
        SN = mexc(Coin, response_mexc)
    elif Sell_name == 'Kucoin':
        SN = kucoin(Coin, response_kucoin)
    elif Sell_name == 'Bitget':
        SN = bitget(Coin, response_bitget)
    elif Sell_name == 'Gateio':
        SN = gateio(Coin)
    elif Sell_name == 'Binance':
        SN = binance(Coin, response_binance)
    else:
        SN = Huobi(Coin, response_huobi)
    return [BN, SN]
# print(getNetwork('Binance', 'Mexc', 'MINA'))


def checkForChain(Buy_name, Sell_name, Coin):
    answer = getNetwork(Buy_name, Sell_name, Coin)
    goods = []
    if answer == False:
        return False
    for a, b in product(answer[0], answer[1]):
        if a[0] == b[0] and a[2]['isWithdrawEnabled'] and a[2]['isDepositEnabled'] and b[2]['isWithdrawEnabled'] and \
                b[2][
                    'isDepositEnabled']:
            goods.append(a)
    if goods != []:
        return min(goods, key=lambda x: x[1])[:2]
    else:
        return False


# print(Huobi('CORE'))
def gen_sign(method, url, query_string=None, payload_string=None):
    key = '2a6305f26c426a27ebf3ce4512b49511'  # api_key
    secret = '61baea814ce98e4dbc1e1a721d051a51fda3bc8551d2efa11556f9cd052b34fe'  # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}
# host = "https://api.gateio.ws"
# prefix = "/api/v4"
# headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
#
# url = '/spot/batch_fee'
# query_param = 'currency_pairs=BTC_USDT,ETH_USDT'
# # for `gen_sign` implementation, refer to section `Authentication` above
# sign_headers = gen_sign('GET', prefix + url, query_param)
# headers.update(sign_headers)
# r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
# print(r.json())
# print(gateio('CNYX'))
