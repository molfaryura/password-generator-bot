'''Telegram bot, which
    generate secure passwords
'''

import secrets

import re

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

