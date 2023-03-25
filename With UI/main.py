from tkinter import *
import os
import random
import json
import base64
from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Passwords Wallet - By Moaz Ahmad")

Label(root, text ='Passwords Wallet', font = 'arial 20 bold').pack()

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()
PasswordMode = StringVar()
PasswordLen = StringVar()

Label(root, font= 'arial 12 bold', text='App Name').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)
Label(root, font = 'arial 12 bold', text ='encryption KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)
Label(root, font = 'arial 12 bold', text ='MODE (Read = r) (Write = w)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)
Entry(root, font = 'arial 10 bold', textvariable = PasswordMode, bg ='ghost white').place(x=290, y = 190)
Label(root, font = 'arial 12 bold', text ='(g = Generate, e - enter)').place(x=60, y = 190)
Entry(root, font = 'arial 10 bold', textvariable = PasswordLen, bg ='ghost white').place(x=290, y = 215)
Label(root, font = 'arial 12 bold', text ='Generated Password Len').place(x=60, y = 215)


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
def Mode():
    if(mode.get() == 'r'):
        with open('Passwords.json', 'r') as f:
            data = json.load(f)
        try:
            password = data[Text.get()]["password"]
        except:
            Result.set("Wrong Name")
            Result.set(Decode(private_key.get(), password))


    elif(mode.get() == 'w'):
        with open("Passwords.json", 'r') as f:
            data = json.load(f)
            if (PasswordMode.get() == "e"):
                y = {Text.get(): {
                    "password": Encode(private_key.get(), Result.get()),
                    "length": len(Result.get())
                }}
            elif (PasswordMode.get() == "g"):
                Gpassword = makePassword(int(PasswordLen.get()))
                Result.set(Gpassword)
                y = {Text.get(): {
                    "password": Encode(private_key.get(), Gpassword),
                    "length": len(Gpassword)
                }}
            else:
                PasswordMode.set("Invalid Mode")
            # data.update(y)
        data.update(y)
        os.remove("Passwords.json")
        with open("Passwords.json", 'w') as f:
            json.dump(data, f, indent=4)


    else:
        Result.set('Invalid Mode')
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    PasswordLen.set("")
    PasswordMode.set("")
def Exit():
    root.destroy()

Button(root, font = 'arial 10 bold', text = 'Password'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 250)
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 250)

root.mainloop()

