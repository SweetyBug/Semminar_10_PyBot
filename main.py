import telebot
from telebot import types #Для кнопок
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from search import *
from add import *
import csv

with open('Token.txt', 'r') as file:
    Token = file.read()

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Что вы хотите сделать?'
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('Добавить студента')
    markup.row('Добавить факультет')
    markup.row('Добавить преподавателя')
    markup.row('Поиск студентов')
    markup.row('Поиск преподавателей')
    markup.row('Показать факультеты')
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mes_from_user(message):
    get_mes = message.text.strip().lower()
    if get_mes == 'показать факультеты':
        bot.send_message(message.chat.id, pr_fac())

bot.polling(none_stop=True)


