# Python36

import random
import string
import hashlib

gen1 = string.digits + string.ascii_lowercase + string.punctuation  # Variable: gen1, contains numbers and lowercase alphabet and punctuation marks.
gen2 = string.digits                                               # Variable: gen2, contains only number.
gen3 = string.ascii_lowercase + string.ascii_uppercase             # Variable: gen3, contains only lowercase and uppercase alphabet.
gen4 = string.punctuation                                          # Variable: gen4, contains only punctuation marks.

print('Random Password Generating Or Hashing.\n')

print ('1. Regular Password, length "10".')
print ('2. Medium Password, length "15".')
print ('3. Strong Password, length "25".')
print ('4. Custom Password, length "Custom".')
print ('5. Only Alphabet, Lower & Upper case Password, length "25".')
print ('6. Only Punctuation Marks Password, length "20".')
print ('7. Only Numbers Password, length "Custom".')
print ('----------------------------------------------------------')
print ('8. Encrypt Your Password With Couple Of Hashing Methods.\n')

que = int(input('Select The Type Of Password You Want, Or To Enrypt [1-8]: '))  # creating our input section. either you want to choose password outputs or encrypting.
print('')             # ignore this it's just for skipping lines.
choice = int(que)     # choice = our input section

if choice == 1:
    print(''.join(random.sample(gen1 * 10, 10)))  # prints a random password length is 10, mixed numbers with alphabet and punctuation marks.

elif choice == 2:
    print(''.join(random.sample(gen1 * 15, 15)))  # prints a random password length is 15, mixed numbers with alphabet and punctuation marks.

elif choice == 3:
    print(''.join(random.sample(gen1 * 25, 25)))  # prints a random password length is 25, mixed numbers with alphabet and punctuation marks.

elif choice == 4:
    custom = int(input('Type the length you want: '))
    print('')
    print(''.join(random.sample(gen1 * custom, custom)))  # prints a random password, mixed numbers with characters and punctuation marks, you choose your own length.

elif choice == 5:
    print(''.join(random.sample(gen3 * 25, 25)))  # prints a random password only alphabet lowercase or uppercase, length is 25.

elif choice == 6:
    print(''.join(random.sample(gen4 * 20, 20)))  # prints a random password only punctuation marks length is 20.

elif choice == 7:
    custom2 = int(input('Type the length you want: '))
    print('')
    print(''.join(random.sample(gen2 * custom2, custom2)))  # prints a random password contains only numbers, you choose your own length.

elif choice == 8:
    print('''Hashing Methods:

1. MD5           
2. SHA-1
3. SHA-224
4. SHA-256
5. SHA-384
6. SHA-512\n''')

    otherchoice = int(input('Select The Hashing Method You Want [1-6]: '))  # enter the hashing algorithm you wanted your password to be hashed/encrypted with.
    print('')

    if otherchoice == 1:
        tohash = input('Write Your Password To Encrypt it with MD5: ')
        hasher = hashlib.md5()
        hasher.update(str(tohash).encode('utf-8'))  # ecnrypts your password with md5.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    elif otherchoice == 2:
        tohash = input('Write Your Password To Encrypt it with SHA-1 : ')
        hasher = hashlib.sha1()
        hasher.update(str(tohash).encode('utf-8'))  # ecrypts your password with sha-1, secure hash algorithm 1.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    elif otherchoice == 3:
        tohash = input('Write Your Password To Encrypt it with SHA-224: ')
        hasher = hashlib.sha224()
        hasher.update(str(tohash).encode('utf-8'))  # ecrypts your password with sha-224, secure hash algorithm 224.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    elif otherchoice == 4:
        tohash = input('Write Your Password To Encrypt it with SHA-256: ')
        hasher = hashlib.sha256()
        hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-256, secure hash algorithm 256.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    elif otherchoice == 5:
        tohash = input('Write Your Password To Encrypt it with SHA-384: ')
        hasher = hashlib.sha384()
        hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-384, secure hash algorithm 384.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    elif otherchoice == 6:
        tohash = input('Write Your Password To Encrypt it with SHA-512: ')
        hasher = hashlib.sha512()
        hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-512, secure hash algorithm 512.
        hashed_password = hasher.hexdigest()
        print('\n[-] Your Hashed Password Is:', hashed_password)

    else:
        print('[-] You must choose any of the displayed hash types [1-6]')

else:
    print('[-] You have only 8 selections [1-8]')
