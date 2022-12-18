import telebot
import requests


bot = telebot.TeleBot("5879537368:AAEfoce8AGy9e64PTeocjJ0tne2idLDx6V0")


@bot.message_handler(commands=['start', 'help'])
def privet(message):
	bot.reply_to(message, "Привет!")


bot.polling()