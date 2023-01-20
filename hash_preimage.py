import hashlib
import os
import random
import string

def random_string_generator(length):
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def hash_preimage(target_string):
    if not all([x in '01' for x in target_string]):
        print("Input should be a string of bits")
        return
    nonce = b'\x00'
    num_of_bits=len(target_string)

    while True:
        string=random_string_generator(random.randint(1,10))
        hash_hex = hashlib.sha256(string.encode('utf-8')).hexdigest()
        hash_bit = bin(eval("0x" + hash_hex))
        if hash_bit[-num_of_bits:]==target_string:
            nonce=string.encode('utf-8')
            break
        else: continue
    return (nonce)





