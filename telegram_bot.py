'''Telegram bot, which
    generate secure passwords
'''

import secrets

def gen_pass(chars, length):
    '''Return randomly generated string
       of certain length
    '''
    chars_tup = (secrets.choice(chars) for _ in range(length))
    return "".join(chars_tup)

