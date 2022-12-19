import telebot
import requests
import requests
import requests
import requests
import requests
import requests
import requests
import requests
import requests
import requests

import json
import lxml
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot("5879537368:AAEfoce8AGy9e64PTeocjJ0tne2idLDx6V0")
def problem():
    url = 'https://problems.ru/view_random.php'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    dock = soup.find("div", {"class": "componentboxcontents"})
    bock=''
    k=1
    while bock=='':
        bock=dock.find_all("p")[k].text
        k+=1
    return bock

@bot.message_handler(commands=['start', 'help'])
def st1(message):
    kb=types.ReplyKeyboardMarkup()
    kn1=types.KeyboardButton(text='Получить задачу с проблемс ру')
    kb.add(kn1)
    bot.send_message(message.chat.id,problem(), reply_markup=kb)
@bot.message_handler(regexp='Получить задачу с проблемс ру')
def st2(message):
    kb = types.ReplyKeyboardMarkup()
    kn1 = types.KeyboardButton(text='Получить задачу с проблемс ру')
    kb.add(kn1)
    bot.send_message(message.chat.id,problem(), reply_markup=kb)

bot.polling()