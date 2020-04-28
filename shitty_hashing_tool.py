#importing modules
import hashlib
import sys
#all functions
def help_text():
    print("-h       :   This help page")
    print("-md5     :   md5 <string>")
    print("-sha1    :   sha1 <string>")
    print("-sha224  :   sha224 <string>")
    print("-sha256  :   sha256 <string>")
    print("-sha384  :   sha384 <string>")
    print("-sha512  :   sha512 <string>")
def md5_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.md5()
    hash.update(text)
    print(hash.hexdigest())
def sha1_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha1()
    hash.update(text)
    print(hash.hexdigest())
def sha224_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha224()
    hash.update(text)
    print(hash.hexdigest())
def sha256_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha256()
    hash.update(text)
    print(hash.hexdigest())
def sha384_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha384()
    hash.update(text)
    print(hash.hexdigest())
def sha512_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha512()
    hash.update(text)
    print(hash.hexdigest())


#main

if(len(sys.argv)==1):
    help_text()
elif(sys.argv[1]=="-md5"):
    md5_decrypt(sys.argv[2])
elif(sys.argv[1]=="-sha1"):
    sha1_decrypt(sys.argv[2])
elif(sys.argv[1]=="-sha224"):
    sha224_decrypt(sys.argv[2])
elif(sys.argv[1]=="-sha256"):
    sha256_decrypt(sys.argv[2])
elif(sys.argv[1]=="-sha384"):
    sha384_decrypt(sys.argv[2])
elif(sys.argv[1]=="-sha512"):
    sha512_decrypt(sys.argv[2])
else:
    print("Wrong input")