#!/bin/python3

"""
 AUTHOR         : SHIHAB ISTIAK SAIKAT
 CREATED        : 08-27-2021
 LAST MODIFIED  : MM-DD-YYYY
 BACKGROUND     : I was studying ansible automation. That time I needed to generate
                  a list of Unix password hashes. Then I wrote the code ;)
"""

import crypt
import sys

file_path = input("Please enter your output file path:\n>>> ")
hash_algo = input("Choose a hashing algorithm ( 6 for SHA-512, 5 for SHA-256, 1 for MD5  ) or hit enter for default:\n>>> ")

def gen_hash():
    f_open = open(file_path, 'a')
    f_open.write("user_list:\n")

    while True:
        user_name = input("Please enter your username:\n>>> ")
        plain_word = input("Please enter your plain password:\n>>> ")

        if hash_algo == "6" or hash_algo =="":
            slt_value = crypt.mksalt(crypt.METHOD_SHA512)
            pw_hash = crypt.crypt(plain_word, salt=slt_value )

        elif hash_algo == "5":
            slt_value = crypt.mksalt(crypt.METHOD_SHA256)
            pw_hash = crypt.crypt(plain_word, salt=slt_value )

        elif hash_algo == "1":
            slt_value = crypt.mksalt(crypt.METHOD_MD5)
            pw_hash = crypt.crypt(plain_word, salt=slt_value )

        else:
            print("\nBad algorithm :(\nTerminated ...\n")
            sys.exit()

        f_open.write(" " * 4 + "- { " + "username: " + user_name + ", " + "pwhash: " + pw_hash + " }" + "\n")

        add_or_out = input("Hit enter to do more or press 'E'/'e' to exit: ")

        if add_or_out == "":
            continue
        else:
            f_open.close()
            print("\nGood bye ...\n")
            sys.exit()

try:
    gen_hash()
except FileNotFoundError:
    print("\nInvalid path detected :(\nPlease enter correct path ...\n")
