#importing modules
import hashlib
import sys
#all functions
def help_text():
    print("-h       :   This help page")
    print("-md5     :   md5 <hash> <wordlist>")
    print("-sha1    :   sha1 <hash> <wordlist>")
    print("-sha224  :   sha224 <hash> <wordlist>")
    print("-sha256  :   sha256 <hash> <wordlist>")
    print("-sha384  :   sha384 <hash> <wordlist>")
    print("-sha512  :   sha512 <hash> <wordlist>")
def md5_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.md5()
    hash.update(text)
    return(hash.hexdigest())
def sha1_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha1()
    hash.update(text)
    return(hash.hexdigest())
def sha224_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha224()
    hash.update(text)
    return (hash.hexdigest())
def sha256_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha256()
    hash.update(text)
    return (hash.hexdigest())
def sha384_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha384()
    hash.update(text)
    return (hash.hexdigest())
def sha512_decrypt(text):
    text=bytes(text,"ascii")
    hash=hashlib.sha512()
    hash.update(text)
    return (hash.hexdigest())


#main
#check if any args given
if(len(sys.argv)==1):
    help_text()
#check if any worsdlist given
if(sys.argv[3] is False):
    print("Enter wordlist")
else:
    try:
        f=open(sys.argv[3],"r")
    except FileNotFoundError:   #check if wordlist id present
        print("Wordlist not Found in current Directory")
    else:
        #FULL WORKING- (JUST COMPARING HASHED TEXTS TO GIVEN)
        content=f.read()
        text=content.split("\n")
        f.close()
        if (sys.argv[1] == "-md5"):
            for word in text:
                hash = md5_decrypt(word)
                if(hash==sys.argv[2]):
                    print("Password found!!:- "+word)
                    break
        elif (sys.argv[1] == "-sha1"):
            for word in text:
                hash = sha1_decrypt(word)
                if (hash == sys.argv[2]):
                    print("Password found!!:- " + word)
                    break
        elif (sys.argv[1] == "-sha224"):
            for word in text:
                hash = sha224_decrypt(word)
                if (hash == sys.argv[2]):
                    print("Password found!!:- " + word)
                    break
        elif (sys.argv[1] == "-sha256"):
            for word in text:
                hash = sha256_decrypt(word)
                if (hash == sys.argv[2]):
                    print("Password found!!:- " + word)
                    break
        elif (sys.argv[1] == "-sha384"):
            for word in text:
                hash = sha384_decrypt(word)
                if (hash == sys.argv[2]):
                    print("Password found!!:- " + word)
                    break
        elif (sys.argv[1] == "-sha512"):
            for word in text:
                hash = sha512_decrypt(word)
                if (hash == sys.argv[2]):
                    print("Password found!!:- " + word)
                    break
        else:
            print("Wrong hash")

