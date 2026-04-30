import random as rd
import string as str
lst = list(str.ascii_letters + str.punctuation + str.digits + " ")
key = lst.copy()
rd.shuffle(key)
#encryption
msg = input("Enter your message: ")
encry = ""
for element in msg:
    encry += key[lst.index(element)]
print(f"Encrypted message: {encry}")
#decryption
msg = input("Enter message to Decrypt: ")
decry = ""
for element in msg:
    decry += lst[key.index(element)]
print(f"Original message is: {decry}")