import random
import string
import base62

CODE_LENGTH = 6

def generate_short_code():
    '''Generate a random short code of length CODE_LENGTH using letters and digits.'''
    short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(CODE_LENGTH))
    return short_code

def convert_to_base_62(number):
    '''Convert a given id to a base-62 encoded string.'''
    return base62.encode(number)


