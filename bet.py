import os 
import time
import re
import getpass
import random

from datetime import datetime
from membreinformation import *
 
def cls():
    os.system('cls')

def today():
    today = datetime.now() 
    formated_data = today.strftime("%Y/%m/%d %H:%M:%S") 
    data['singuptime'] = formated_data

def testpassword(username,password,confirmpassword) :
    username = input('UserName : ')
    a = memory.keys()
    while username in a :
        cls()
        print('This UserName has been used before ... !\nTry Something else ...')
        username = input('UserName : ')
    password = getpass.getpass('Your Password : ')
    confirmpassword = getpass.getpass('Enter Your Password again : ')
    while password != confirmpassword :
        cls()
        Red()
        print('try again ...')
        wait()
        Blue()
        print(f'UserName : {username}')
        password = getpass.getpass('Your Password : ')
        confirmpassword = getpass.getpass('Enter Your Password again : ')
    data['username'] = username
    data['password'] = password
    user_id = random.randint(1,10)
    data['user_id'] = user_id

   

def Rightname(name,lastname):
    name = input('Your First Name : ')
    lastname = input('Last Name : ')
    x = re.findall("[!|@|#|$|%|^|&|*]", name )
    y = re.findall("[!|@|#|$|%|^|&|*]", lastname )
    while (x) or (y):
        cls()
        print('Please Dont Use This Signs (!@#$%^&*)')
        name = input('Your First Name : ')
        lastname = input('Last Name : ')
        x = re.findall("[!|@|#|$|%|^|&|*]", name )
        y = re.findall("[!|@|#|$|%|^|&|*]", lastname )
    data['name'] = name
    data['lastname'] = lastname

def email(email):
    email = input('Enter Your Email : ') 
    w = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email)
    while not(w):
        cls()
        email = input('Enter Your Email again : ') 
        w = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email)
    data['email'] = email   

def phonenumber(phonenumber):
    phonenumber = input("Enter your phone number : ") 
    l = len(phonenumber)
    y = re.findall("[0-9]", phonenumber )
    while l != 11 or not(y)  :
        cls()
        phonenumber = input("Enter your phone number again: ")
        l = len(phonenumber)
        y = re.findall("[0-9]", phonenumber )
    data['phonenumber'] = phonenumber


def postalcode(postalcode):
    postalcode = input('Enter Your PostalCode : ')
    a = len(postalcode)
    b = re.findall("[0-9]-[0-9]", postalcode )
    c = postalcode.find('-')
    while a != 11 or not(b) or c != 5 :
        postalcode = input('Enter Your PostalCode again : ')
        a = len(postalcode)
        b = re.findall("[0-9]-[0-9]", postalcode)
        c = postalcode.find('-')


def wait():
    time.sleep(1)

def Blue():
    os.system("color 9")

def Red():
    os.system("color C")

def Bright():
    os.system("color F")


data = {'username':'' , 'password': '','name':'' ,'lastname':'','email':'','phonenumber':'','user_id':'','singuptime':'' }

myfile = open('membreinformation.py')
mywork = myfile.read()
myfile.close()
a = mywork.count('data')
b = a + 1

def myfilee():  
    myfile = open('membreinformation.py','r')
    filetxt = myfile.read()
    myfile.close()
    c = filetxt.splitlines()
    txt = ('  "%s" :'% data['username'] +
     "{'username':'%s' , " % data['username'] +
     "'password': '%s'," % data['password'] +
     "'name':'%s' ," % data['name'] +
     "'lastname':'%s'," % data['lastname'] +
     "'email':'%s'," % data['email'] +
     "'phonenumber':'%s'," % data['phonenumber'] +
     "'user_id':'%s'  ," % data['user_id'] +
     "'singuptime':'%s' }," % data['singuptime'])
    c.insert(1,txt)  
    i=0
    a=""
    for i in range(0,len(c)):
        a=a+c[i]+'\n'
    myfile2 = open ('membreinformation.py','w')      
    myfile2.write(a)
    myfile2.close()

