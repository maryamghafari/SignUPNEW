import os 
import time
import re
import getpass
import random
import smtplib

from membreinformation import *

def cls():
    os.system('cls')

def wait():
    time.sleep(0.6)

def wait1():
    time.sleep(0.2)

def Blue():
    os.system("color 9")

def Red():
    os.system("color C")

def Bright():
    os.system("color F")


           

def testpassword(username,password) :
    cls()
    x = 0
    username = input('UserName : ')
    password = getpass.getpass('Your Password : ')
    t = memory.keys()
    x += 1
    while username not in t :
        cls()
        Red()
        print('try again ...your username not found ...')
        wait()
        Blue()
        username = input('UserName : ')
        password = getpass.getpass('Your Password : ')
        x += 1
    a = memory[username]
    s = a['password']
    email = a['email']
    while password != s :
        cls()
        print(f'UserName : {username}')
        password = getpass.getpass('Enter Your Password again : ')
        forgotpassword = input('Forgot password ?!(yes or no)')
           
        if forgotpassword == 'yes' :
            print('A code has been sent to your email to change your password ')
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import smtplib

            msg = MIMEMultipart()

            password = "M@rMar1379"
            msg['From'] = "m2000ghafari@gmail.com"
            msg['To'] = "eng.maryamkhorram@gmail.com"
            msg['Subject'] = "Password change code"
            keycod = random.randint(9,100)
            message = f"Hello, This is a test from mary app!\n This is code for register password: {keycod}"

            msg.attach( MIMEText(message, 'plain') )

            server = smtplib.SMTP('smtp.email.com: 25')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail( msg['From'], msg['To'], msg.as_string() )

            server.quit()
 
            

        x += 1    
    print('Welcome my friend ...')
    wait()
    print(f'{x} times trying to login .')
    wait()
    print('These is your information ...')
    wait1()
    for item_key , item_value in a.items() :
        print(f'Your {item_key} is : {item_value}')
        wait1()
        wait
    i = a['user_id']
    v = memory.values()
    if int(i) < 4 :
        print('Because you are a special user you can see all users ...')
        for x in v :
            a = x
            for item_key , item_value in a.items() :
                print(f'the {item_key} is : {item_value}')
            print(f'\n')     
            wait1()
    else:
        print('...')              


