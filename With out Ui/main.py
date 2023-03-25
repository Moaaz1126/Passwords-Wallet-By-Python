import os
import random
import json
import requests
import base64

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def makePassword(lenth):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-@$"
    all = lower + upper + NUMBER + Symbol
    # lenth = 10
    password = "".join(random.sample(all, lenth))
    return password
def sendpassword():
    use = input("Do You Wont To Read Or Write (Read = r) (Write = w) : ")
    if(use == "r") :
        Read()
    elif(use == "w"):
        Write()
def Read():
    with open('Passwords.json', 'r') as f:
        data = json.load(f)
    try:
        app = input("Please Enter An Name : ")
        password = data[app]["password"]
        key = input("Enter Your encryption code //If The Password Wrong You Entered Wrong encryption code: ")
        Decode(key, password)
        print("Password is : " + Decode(key, password))
    except:
        print("Wrong Name")
    sendpassword()
def Write():
    app = input("Enter The App Name : ")
    password = input("Generate Password Or Enter Password (Generate g) (Enter e): ")
    key = input("Enter Your encryption code //If The Password Wrong You Entered Wrong encryption code: ")
    if(password == "e"):
        EnteredPassword = input("Enter Password : ")
    else:
        lenth = input("Enter Length : ")
        passwordCode = makePassword(int(lenth))
        print(passwordCode)
    with open("Passwords.json", 'r') as f:
        data = json.load(f)
        if (password == "e"):
            y = {app: {
                "password": Encode(key, EnteredPassword),
                "length": len(EnteredPassword)
            }}
        else:
            y = {app: {
                "password": Encode(key, passwordCode),
                "length": lenth
            }}

        data.update(y)

    os.remove("Passwords.json")
    with open("Passwords.json", 'w') as f:
        json.dump(data, f, indent=4)
    sendpassword()
sendpassword()