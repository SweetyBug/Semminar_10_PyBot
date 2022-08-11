import telebot
import random
from tic_tac_toe import *

bot = telebot.TeleBot('5502799886:AAGvSC6DlKPxTN_HduTjN6gh74NKcxyuFUk')
table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
b = ''


@bot.message_handler(commands=['start'])
def start(message):
    global b
    global table
    b = ''
    table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    name = f'Привет, {message.from_user.first_name}!\nТвой противник - бот Сережа :)\nЧтобы у тебя была фора, ты ходишь первый.'
    bot.send_message(message.chat.id, name)
    bot.send_message(message.chat.id, pr(table))



@bot.message_handler(content_types=['text'])
def text(message):
    global b
    global table
    a = message.text
    a = list(map(int, a.split()))
    if b == "Поздравляю, вы победили!" or b == 'Упс... Кажется вы проиграли.' or b == 'Ничья':
        bot.send_message(message.chat.id, pr(table))
        bot.send_message(message.chat.id, b)
    else:
        if table[a[0]][a[1]] == '*':
            table[a[0]][a[1]] = 'x'
            if '*' in table[0] or '*' in table[1] or '*' in table[2]:
                bot_go(table)
            bot.send_message(message.chat.id, pr(table))
            b = game(table)
            bot.send_message(message.chat.id, b)
        else:
            bot.send_message(message.chat.id, 'Эта ячейка занята, введите другие значение!')

bot.polling(none_stop=True)


