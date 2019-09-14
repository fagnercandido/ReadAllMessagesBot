# coding=utf-8

import os
import telebot
import urllib
import json

botRead = telebot.TeleBot(os.environ["BOT_READ_ALL_MESSAGES"])

@botRead.message_handler(commands=['start', 'help'])
def send_start_message(message):
    botRead.reply_to(message, "Olá, eu sou o Bot 'Read All Messages' \n"
                          "Diariamente irei enviar as mensagens não lidas para seu e-mail")
                    
botRead.polling()