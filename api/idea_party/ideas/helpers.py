import random

def give_me_id():
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ1234567890"
    return ''.join([random.choice(valid_chars) for _ in range(0, 5)])