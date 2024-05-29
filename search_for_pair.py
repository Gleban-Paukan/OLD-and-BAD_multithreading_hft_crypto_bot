import requests


def Get_All_Pair(Pair):
    a = []
    try:
        answer = requests.get(f'https://api.mexc.com/api/v3/depth', params={'symbol': f'{Pair}USDT'}).json()
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) > 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append([prodaja, pokupka,
                  f'https://www.mexc.com/ru-RU/exchange/{Pair}_USDT?_from=search_spot_trade', 'Mexc', V])
    except Exception as er:
        pass
    try:
        answer = requests.get(f'https://api.gateio.ws/api/v4/spot/order_book',
                              params={'currency_pair': f'{Pair}_USDT'}).json()
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append([prodaja, pokupka,
                  f"https://www.gateio.ws/ru/trade/{Pair}_USDT", 'Gateio', V])
    except:
        pass
    try:
        answer = \
            requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level2_20',
                         params={'symbol': f'{Pair}-USDT'}).json()[
                'data']
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append(
            [prodaja, pokupka, f'https://www.kucoin.com/ru/trade/{Pair}-USDT?spm=kcWeb.B1homepage.Header4.1', 'Kucoin',
             V])
    except:
        pass
    try:
        answer = \
            requests.get(f'https://api.binance.com/api/v3/depth', params={'symbol': f'{Pair}USDT'}).json()
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append([prodaja, pokupka,
                  f'https://www.binance.com/en/trade/{Pair}_USDT?_from=markets&theme=dark&type=spot', 'Binance', V])
    except:
        pass
    try:
        answer = \
            requests.get(f'https://api.huobi.pro/market/depth?symbol={Pair.lower}usdt&type=step0').json()['tick']
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append([prodaja, pokupka,
                  f'https://www.huobi.com/ru-ru/exchange/{Pair.lower()}_usdt', 'Huobi', V])  # second number = size!
    except Exception as er:
        pass
    try:
        answer = \
            requests.get(
                f'https://api.bitget.com/api/spot/v1/market/depth?symbol={Pair}USDT_SPBL&type=step0&limit=100').json()[
                'data']
        a1 = answer['bids']
        w = answer['asks']
        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
        a.append([prodaja, pokupka, f'https://www.bitget.com/ru/spot/{Pair}USDT_SPBL?type=spot', 'Bitget', V])
    except:
        pass
    if a != []:
        try:
            return [round((max(a, key=lambda x: x[0])[0] / min(a, key=lambda x: x[1])[1]) * 100 - 100, 3), Pair,
                    min(a, key=lambda x: x[1])[2], max(a, key=lambda x: x[0])[2],
                    min(a, key=lambda x: x[1])[3], max(a, key=lambda x: x[0])[3], min(a, key=lambda x: x[1])[1],
                    max(a, key=lambda x: x[0])[0], min(a, key=lambda x: x[1])[4]]
        except Exception as er:
            print(a)
            print(er)
            return [0]
    else:
        return [0]


def Search_The_Best(Base):
    result = []
    for Pair in Base:
        result.append(Get_All_Pair(Pair))
    return result

