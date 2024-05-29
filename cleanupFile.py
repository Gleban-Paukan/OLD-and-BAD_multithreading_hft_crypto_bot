import grequests
import requests
import threading
import time
def GATE_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[c]
            answer = i.json()
            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
        except Exception as er:
            print(er, i.text, 'Gate')
    flag[name] = True
def BINANCE_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[c]
            if 'Huobi' in name:
                Pair = Pair.lower()
            answer = i.json()
            if 'data' in answer:
                answer = i.json()['data']
            if 'tick' in answer:
                answer = answer['tick']
            if 'result' in answer:
                answer = answer['result']

            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
        except Exception as er:
            print(er, i.text, 'Binance')
    flag[name] = True
def HUOBI_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[c]
            if 'Huobi' in name:
                Pair = Pair.lower()
            answer = i.json()
            if 'data' in answer:
                answer = i.json()['data']
            if 'tick' in answer:
                answer = answer['tick']
            if 'result' in answer:
                answer = answer['result']

            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
        except Exception as er:
            print(er, i.text, 'Huobi')
    flag[name] = True
def MEXC_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[c]
            if 'Huobi' in name:
                Pair = Pair.lower()
            answer = i.json()
            if 'data' in answer:
                answer = i.json()['data']
            if 'tick' in answer:
                answer = answer['tick']
            if 'result' in answer:
                answer = answer['result']

            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
        except Exception as er:
            print(er, i.text, 'Mexc')
    flag[name] = True
def ByBit_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            # print(i.json())
            Pair = PairBase[c]
            if 'Huobi' in name:
                Pair = Pair.lower()
            answer = i.json()
            if 'data' in answer:
                answer = i.json()['data']
            if 'tick' in answer:
                answer = answer['tick']
            if 'result' in answer:
                answer = answer['result']

            a1 = answer['b']
            w = answer['a']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
            # print(Pair, c)
        except Exception as er:
            print(er, i.text, 'ByBit')
    flag[name] = True
def KUCOIN_SEARCH(Base, PairBase, link, name, ID):
    flag[name] = False
    response = (grequests.get(url) for url in Base)
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[c]
            if 'Huobi' in name:
                Pair = Pair.lower()
            answer = i.json()
            if 'data' in answer:
                answer = i.json()['data']
            if 'tick' in answer:
                answer = answer['tick']
            if 'result' in answer:
                answer = answer['result']

            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[c]].append(
                [prodaja, pokupka, link.format(Pair), name, V])
        except Exception as er:
            print(er, i.text, 'Kucoin')
    flag[name] = True
def bitFUCK(Base, PairBase, ID):
    counter = 0
    flag['Bitget'] = False
    for x in range(len(Base)//10):
        response = (grequests.get(url) for url in Base[x*10:(x+1)*10])
        for c, i in enumerate(grequests.map(response)):
            try:
                Pair = PairBase[counter]
                answer = i.json()['data']
                a1 = answer['bids']
                w = answer['asks']
                prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
                pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
                V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                         float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
                # print(Pair, f'https://www.bitget.com/ru/spot/{Pair}USDT_SPBL?type=spot', prodaja, pokupka)
                BIG_DICT[ID][PairBase[counter]].append([prodaja, pokupka, f'https://www.bitget.com/ru/spot/{Pair}USDT_SPBL?type=spot', 'Bitget', V])
                counter += 1
            except Exception as er:
                print(er, i.text, 'Kucoin')
                counter += 1
        time.sleep(1)
    response = (grequests.get(url) for url in Base[len(Base) - len(Base) % 10:])
    for c, i in enumerate(grequests.map(response)):
        try:
            Pair = PairBase[counter]
            answer = i.json()['data']
            a1 = answer['bids']
            w = answer['asks']
            prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
            pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
            V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                     float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
            BIG_DICT[ID][PairBase[counter]].append([prodaja, pokupka, f'https://www.bitget.com/ru/spot/{Pair}USDT_SPBL?type=spot', 'Bitget', V])
            counter += 1
            flag['Bitget'] = True
        except Exception as er:
            print(er, i.text, 'Kucoin')
            counter += 1

Kucoin_base = [i["baseCurrency"] for i in requests.get('https://api.kucoin.com/api/v1/symbols').json()['data'] if i['quoteCurrency'] == 'USDT' and '3L' != i['baseCurrency'][len(i['baseCurrency']) - 2: len(i['baseCurrency'])] and '3S' != i['baseCurrency'][len(i['baseCurrency']) - 2: len(i['baseCurrency'])]]
Mexc_base = [i['symbol'][:-4] for i in requests.get('https://api.mexc.com/api/v3/exchangeInfo').json()['symbols'] if 'USDT' in i['symbol'] and 'SPOT' in i["permissions"] and '3L' != i['symbol'][:-4][len(i['symbol'][:-4]) - 2: len(i['symbol'][:-4])] and '3S' != i['symbol'][:-4][len(i['symbol'][:-4]) - 2: len(i['symbol'][:-4])]]
Gateio_base = [i['currency'] for i in requests.get('https://api.gateio.ws/api/v4/spot/currencies').json() if '_' not in i['currency'] and '3L' != i['currency'][len(i['currency']) - 2: len(i['currency'])] and '3S' != i['currency'][len(i['currency']) - 2: len(i['currency'])]]
Binance_base = [i['baseAsset'] for i in requests.get('https://api.binance.com/api/v3/exchangeInfo').json()['symbols'] if 'USDT' in i['symbol'] and "SPOT" in i["permissions"]]
# Huobi_base = [i['bc'].upper() for i in requests.get('https://api.huobi.pro/v2/settings/common/symbols').json()['data'] if i['qc'] == 'usdt' and '3l' != i['bc'][len(i['bc']) - 2: len(i['bc'])] and '3s' != i['bc'][len(i['bc']) - 2: len(i['bc'])]]
Bitget_base = [i['baseCoin'] for i in requests.get('https://api.bitget.com/api/spot/v1/public/products').json()['data'] if i['quoteCoin'] == 'USDT']
ByBit_Base = [j for j in [i['symbol'][:len(i['symbol']) - 4] for i in requests.get('https://api.bybit.com/v5/market/tickers?category=spot').json()['result']['list']] if '2S' not in j and '2L' not in j and '3S' not in j and '3L' not in j]# BIG_DATA_BASE = set(Bitget_base + Kucoin_base + Mexc_base + Gateio_base + Huobi_base + Binance_base + ByBit_Base)
# BIG_DATA_BASE = set(Bitget_base + Kucoin_base  + Gateio_base + Binance_base + ByBit_Base + Huobi_base)
BIG_DATA_BASE = set(Bitget_base + Kucoin_base  + Gateio_base + Binance_base + ByBit_Base + Mexc_base)
Kucoin = [f'https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol={Pair}-USDT' for Pair in Kucoin_base]
Mexc = [f'https://api.mexc.com/api/v3/depth?symbol={Pair}USDT' for Pair in Mexc_base]
ByBit = [f'https://api.bybit.com/v5/market/orderbook?symbol={Pair}USDT&category=spot&limit=150' for Pair in ByBit_Base]
Gateio = [f'https://api.gateio.ws/api/v4/spot/order_book?currency_pair={Pair}_USDT' for Pair in Gateio_base]
Binance = [f'https://api.binance.com/api/v3/depth?symbol={Pair}USDT' for Pair in Binance_base]
# Huobi = [f'https://api.huobi.pro/market/depth?symbol={Pair.lower()}usdt&type=step0' for Pair in Huobi_base]
Bitget = [f'https://api.bitget.com/api/spot/v1/market/depth?symbol={Pair}USDT_SPBL&type=step0&limit=100' for Pair in Bitget_base]
BIG_DICT = {}
small_DICT = {}
ev = threading.Event()
flag = {'Kucoin': False, 'Mexc': False, 'ByBit': False, 'Gateio': False, 'Binance': False, 'Huobi': False, 'Bitget': False}
def bigDEF(ID):
    BitFuck_flag = False
    Gateio_flag = False
    Kucoin_flag = False
    Binance_flag = False
    ByBit_flag = False
    Mexc_flag = False
    Huobi_flag = False
    for thread in threading.enumerate():
        print(thread.name)
        if 'bitFUCK' in thread.name:
            BitFuck_flag = True
        elif 'GATE' in thread.name:
            Gateio_flag = True
        elif 'BINANCE' in thread.name:
            Binance_flag = True
        elif 'KUCOIN' in thread.name:
            Kucoin_flag = True
        elif 'HUOBI' in thread.name:
            Huobi_flag = True
        elif 'ByBit' in thread.name:
            ByBit_flag = True
    if not Kucoin_flag:
        st1 = threading.Thread(target=KUCOIN_SEARCH, args=(Kucoin, Kucoin_base, 'https://www.kucoin.com/ru/trade/{}-USDT?spm=kcWeb.B1homepage.Header4.1', 'Kucoin', ID))
        st1.start()
    if not Mexc_flag:
        st2 = threading.Thread(target=MEXC_SEARCH, args=(Mexc, Mexc_base, 'https://www.mexc.com/ru-RU/exchange/{}_USDT?_from=search_spot_trade', 'Mexc', ID))
        st2.start()
    if not Gateio_flag:
        st3 = threading.Thread(target=GATE_SEARCH, args=(Gateio, Gateio_base, 'https://www.gateio.ws/ru/trade/{}_USDT', 'Gateio', ID))
        st3.start()
    if not Binance_flag:
        st4 = threading.Thread(target=BINANCE_SEARCH, args=(Binance, Binance_base, 'https://www.binance.com/en/trade/{}_USDT?_from=markets&theme=dark&type=spot', 'Binance', ID))
        st4.start()
    # if not Huobi_flag:
    #     st5 = threading.Thread(target=HUOBI_SEARCH, args=(Huobi, Huobi_base, 'https://www.huobi.com/ru-ru/exchange/{}_usdt', 'Huobi', ID))
    #     st5.start()
    if not BitFuck_flag:
        st6 = threading.Thread(target=bitFUCK, args=(Bitget, Bitget_base, ID))
        st6.start()
    if not ByBit_flag:
        st7 = threading.Thread(target=ByBit_SEARCH, args=(ByBit, ByBit_Base, 'https://www.bybit.com/trade/usdt/{}USDT', 'ByBit', ID))
        st7.start()
    start = time.time()
    print(flag)
    while not flag['Kucoin']:
        if time.time() - start >= 400:
            print('KUCOIN '*10)
            print(flag)
            return
        time.sleep(.5)
    print('1')
    while not flag['Mexc']:
        if time.time() - start >= 400:
            return
        time.sleep(.5)
    print('2')
    while not flag['Gateio']:
        if time.time() - start >= 400:
            print('GATEIO '*10)
            return
        time.sleep(.5)
    start = time.time()
    while not flag['Binance']:
        if time.time() - start >= 400:
            print('BINANCE '*10)
            return
        time.sleep(.5)
    # while not flag['Huobi']:
    #     if time.time() - start >= 400:
    #         print('HUOBI '*10)
    #         return
    #     time.sleep(.5)
    while not flag['ByBit']:
        if time.time() - start >= 400:
            print('ByBit '*10)
            return
        time.sleep(.5)
    print('0')
    # print('/' * 60)
    # for thread in threading.enumerate():
    #     print(thread.name)
    # print('?'*60)
def last_def(ID):
    for i in BIG_DATA_BASE:
        small_DICT[i] = []
    flag = {'Kucoin': False, 'Mexc': False, 'ByBit': False, 'Gateio': False, 'Binance': False, 'Huobi': False,
            'Bitget': False}
    BIG_DICT[ID] = small_DICT
    bigDEF(ID)
    # print('-'*70)
    # print(BIG_DICT)
    try:
        for i in BIG_DICT[ID]:
                Pair = i
                a = BIG_DICT[ID][i]
                if a != []:
                    BIG_DICT[ID][i] = [round((max(a, key=lambda x: x[0])[0] / min(a, key=lambda x: x[1])[1]) * 100 - 100, 3), Pair,
                                    min(a, key=lambda x: x[1])[2], max(a, key=lambda x: x[0])[2],
                                    min(a, key=lambda x: x[1])[3], max(a, key=lambda x: x[0])[3], min(a, key=lambda x: x[1])[1],
                                    max(a, key=lambda x: x[0])[0], min(a, key=lambda x: x[1])[4]]
        result = []
        for i in BIG_DICT[ID]:
            if BIG_DICT[ID][i] != []:
                if BIG_DICT[ID][i][0] < 50:
                    result.append(BIG_DICT[ID][i])
        output = sorted(result, reverse=True)[:30]
        return output
    except Exception as er:
        print(er)