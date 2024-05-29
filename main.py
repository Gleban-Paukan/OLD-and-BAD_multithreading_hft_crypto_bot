import datetime
import threading
import grequests
import requests

ev = threading.Event()
ev.set()
from cleanupFile import last_def
import telebot
from telebot import types
import coin_base
import Scratch_file
import sys
import os
import re
from requests import ConnectionError, ReadTimeout

bot = telebot.TeleBot('')
bot.parse_mode = 'html'
stable_dict = {}
obnulator = {}
spread_dict = {}



@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.type == 'private':
        with open('users_id.txt', 'r') as users_id:
            user_set = set()
            for i in users_id:
                user_set.add(i.replace('\n', ''))
        if str(message.chat.id) not in user_set:
            with open('users_id.txt', 'a') as users_id:
                users_id.write(str(message.chat.id) + '\n')
            with open('Spread_filter.txt', 'a') as file:
                file.write(str(message.chat.id) + ' ' + '0' + '\n')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('📌️ Добавить фильтр'), types.KeyboardButton('📕 Инструкция'))
        bot.send_message(message.chat.id, f'Привет. Твой ID <code>{message.chat.id}</code>', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Начать арбитраж!':
            bot.send_message(message.chat.id, 'Арбитраж запущу. Очень надеюсь на профиты :D')
            for _ in range(10000):
                thr1 = threading.Thread(target=busyone, args=[message])
                thr1.start()
                thr1.join()
                print(_)
        elif message.text == '📌️ Добавить фильтр':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton('➗ Спред', callback_data='Spread'))
            bot.send_message(message.chat.id, 'Выберите <b>фильтр</b>.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if 'check' in call.data:
            try:
                print('qweqwe')
                Coin, Buy_Name, Sell_Name, fee, network = re.search(':(.+?):', call.data).group()[1:-1].split()
                fee = float(fee)
                urls = [coin_base.Coin_dict(Buy_Name, Coin), coin_base.Coin_dict(Sell_Name, Coin)]
                url1, url2 = coin_base.Link_dict(Buy_Name, Coin), coin_base.Link_dict(Sell_Name, Coin)
                for c, i in enumerate(requests.get(url) for url in urls):
                    answer = i.json()
                    if 'data' in answer:
                        answer = i.json()['data']
                        a1 = answer['bids']
                        w = answer['bids']
                    elif 'tick' in answer:
                        answer = answer['tick']
                        a1 = answer['bids']
                        w = answer['asks']
                    elif 'result' in answer:
                        answer = answer['result']
                        a1 = answer['b']
                        w = answer['a']
                    else:
                        a1 = answer['bids']
                        w = answer['asks']
                    if c == 0:
                        pokupka = float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[0])
                        V = min([float(min([i for i in w if float(i[0]) * float(i[1]) >= 200])[1]),
                                 float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[1])])
                        print(pokupka)
                    else:
                        prodaja = float(max([i for i in a1 if float(i[0]) * float(i[1]) >= 200])[0])
                        print(prodaja)
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(
                    types.InlineKeyboardButton('✅ Проверить курс',
                                               callback_data=f'check:{Coin} {Buy_Name} {Sell_Name} {fee} {network}:'))
                bot.edit_message_text(message_id=call.message.id, chat_id=call.message.chat.id,
                                      text=f'<b>🔑  Монета <i>{Coin}</i>, спред <ins>{round(((V * (prodaja / pokupka - 1) * prodaja - fee * pokupka) / (V * pokupka)) * 100, 2)} %</ins></b>.\n\n💎 Закупка на <a href="{url1}"> {Buy_Name}</a>, продажа на <a href="{url2}"> {Sell_Name} </a>\n\nЦена покупки: <code>{pokupka}</code>'
                                           f'\n\nЦена продажи: <code>{prodaja}</code>\n\n<b>Сеть</b>: {network}, комиссия: {round(fee * pokupka, 2)}\n<b>Итоговый профит</b>: {round(V * (prodaja / pokupka - 1) * prodaja - fee * pokupka, 2)}, <b>объем: </b>{round(V * pokupka)} USDT\n<i>Последнее измение {datetime.datetime.now().strftime("%H:%M")}</i>',
                                      disable_web_page_preview=True, reply_markup=markup)
            except Exception as er:
                print('qweqweq')
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(
                    types.InlineKeyboardButton('✅ Проверить курс',
                                               callback_data=f'check:{Coin} {Buy_Name} {Sell_Name} {fee} {network}:'))
                bot.edit_message_text(message_id=call.message.id, chat_id=call.message.chat.id,
                                      text=f'{call.message.text}\nСообщение изменить не удалось ',
                                      disable_web_page_preview=True, reply_markup=markup)
                print(er)
        elif call.data == 'Spread':
            bot.send_message(call.message.chat.id, 'Введите минимальный спред в процентах. Например, 1.5')
            bot.register_next_step_handler(call.message, Spread_filter)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


def Spread_filter(message):
    try:
        with open('Spread_filter.txt') as file:
            for line in file:
                key, *value = line.split()
                spread_dict[key] = value[0]
        with open('Spread_filter.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(str(message.chat.id) + ' ' + spread_dict[str(message.chat.id)],
                                    str(message.chat.id) + ' ' + message.text)
        with open('Spread_filter.txt', 'w') as f:
            f.write(new_data)
        bot.send_message(message.chat.id, 'Фильтр добавлен <b>успешно</b>.')
    except Exception as er:
        print(er)
        bot.send_message(message.chat.id, 'Произошла <b>ошибка</b>. Попробуйте ещё раз.')


def busyone(message):
    with open('users_id.txt', 'r') as users_id:
        user_set = set()
        for i in users_id:
            user_set.add(i.replace('\n', ''))
    with open('Spread_filter.txt') as file:
        for line in file:
            key, *value = line.split()
            spread_dict[key] = value[0]
    print(datetime.datetime.now().strftime("%H:%M"))
    for i in last_def(message.chat.id):
        try:
            answer = Scratch_file.checkForChain(i[4], i[5], i[1])
            if 50 > i[0] > 0.3 and i[1] not in coin_base.ErrorBase() and answer != False and round(
                    i[8] * (i[7] / i[6] - 1) * i[7] - answer[1] * i[6], 2) >= 2.5:
                for z in user_set:
                    print(z, spread_dict)
                    if float(spread_dict[z]) <= (
                            ((i[8] * (i[7] / i[6] - 1) * i[7] - answer[1] * i[6]) / (i[8] * i[6])) * 100):
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        markup.add(
                            types.InlineKeyboardButton('✅ Проверить курс',
                                                       callback_data=f'check:{i[1]} {i[4]} {i[5]} {round(answer[1] * i[6], 2)} {answer[0]}:'))
                        bot.send_message(z,
                                         f'<b>🔑  Монета <i>{i[1]}</i>, спред <ins>{round(((i[8] * (i[7] / i[6] - 1) * i[7] - answer[1] * i[6]) / (i[8] * i[6])) * 100, 2)} %</ins></b>.\n\n💎 Закупка на <a href="{i[2]}">{i[4]}</a>, продажа на <a href="{i[3]}">{i[5]} </a>\n\nЦена покупки: <code>{i[6]}</code>'
                                         f'\n\nЦена продажи: <code>{i[7]}</code>\n\n<b>Сеть</b>: {answer[0]}, комиссия: {round(answer[1] * i[6], 2)}\n<b>Итоговый профит</b>: {round(i[8] * (i[7] / i[6] - 1) * i[7] - answer[1] * i[6], 2)}, объем: {round(i[8] * i[6])} USDT',
                                         disable_web_page_preview=True, disable_notification=True, reply_markup=markup,
                                         protect_content=True)
        except Exception as er:
            print(er)


try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
