import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(str(random.choice(chars)) for x in range(length))