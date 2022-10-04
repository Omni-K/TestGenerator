import csv
from random import shuffle, randint, choice
from pprint import pprint
from uuid import uuid1
import datetime

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def generate_variant(n: int):
    numbers = list(range(64, 1024))
    shuffle(numbers)
    r = []
    for i in range(n):
        t = randint(0, 1)
        b = choice((2, 8, 16))
        q = convert_base(numbers[i],
                         from_base=t * 10 + b * ((t + 1) % 2),
                         to_base=t * b + 10 * ((t + 1) % 2))
        a = convert_base(numbers[i],
                         to_base=t * 10 + b * ((t + 1) % 2),
                         from_base=t * b + 10 * ((t + 1) % 2))
        r.append((q, t, b, a))
    return r

def to_text(tup: tuple):
    q, t, b, a = tup
    s = f'Переведите число {q} из СС с основанием {t * b + 10 * ((t + 1) % 2)} в СС с основанием {t * 10 + b * ((t + 1) % 2)}'
    return s, a


for e in generate_variant(5):
    print(to_text(e))

def generate_variant_files(quantity=16):
    var_id = f"{datetime.date.today()}-{'-'.join(str(uuid1()).split('-')[1:3])}"
    tasks = [to_text(i) for i in generate_variant(quantity)]
    f_q = open(f'{var_id}_q.txt', 'w')
    f_a = open(f'{var_id}_a.txt', 'w')
    for tsk in tasks:
        f_q.write(tsk[0]+'\n')
        f_a.write(str(tsk[1])+'\n')
    f_a.close()
    f_q.close()

generate_variant_files()

