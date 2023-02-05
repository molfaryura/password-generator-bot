'''Telegram bot, which
    generate secure passwords
'''

import os

import secrets

import re

import string

import telebot

from dotenv import load_dotenv

def gen_pass(chars, length):
    '''Return randomly generated string
       of certain length
    '''
    chars_tup = (secrets.choice(chars) for _ in range(length))
    return "".join(chars_tup)


def is_password_valid(string_pass):
    '''Verify that password contains
        at leats one uppercase letter,
        lowercase letter, number, and
        a special symbold
    '''
    reg_ex = r'^(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])'
    return re.search(pattern=reg_ex, string=string_pass) is not None

# characters from which the password will be generated
symbols = string.printable[:-15]

load_dotenv()

token = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start(message):
    start_text = (
        f'Hello <b>{message.from_user.first_name}</b>,\n'
        'Welcome to the Password Generator Bot!\n'
        'Here you can generate a very secure password.\n\n'

        '/password - generate a password the length you want.'
    )
    bot.send_message(message.chat.id, start_text,
                     parse_mode='html')
    

@bot.message_handler(commands=['start'])
def ask(message):
    pass_message = (
        'This password will contain at least'
        'one uppercase letter, '
        'a lower case letter, '
        'a number, and a special symbol.\n\n'
        'Please type the length of the password you want(from 4 to 40)'
    )
    ask_user = bot.send_message(message.chat.id, pass_message)
    bot.register_next_step_handler(ask_user, password_foo)

# On the next step the 'password_foo' function should be created! 


if __name__ == '__main__':
    bot.polling(non_stop=True)
