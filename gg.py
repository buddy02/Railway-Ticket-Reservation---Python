
import random

def res():
    print('Enter your date of departure:')
    print('DD/MM/YYYY:')
    da=input()
    print('Class:')
    print('AC First Class')
    print('First Class')
    print('AC 2 Tier')
    print('AC 3 Tier')
    print('Sleeper')
    cla=input('Enter Class: ')
    print('Reservation Type:')
    print('General')
    print('Ladies')
    print('Lower Berth/Sr.citizen')
    print('Person with disability')
    print('Tatkal')
    print('Premium Tatkal')
    rety=input('Enter Reservation type: ')
    print('Enter your details')
    name=input('Enter your name: ')
    age=int(input('Enter your age: '))
    sex=input('Enter your gender: ')
    print('** Your ticket is confirmed **')
    print(name)
    print(age)
    print(sex)
    print('From:',sdest)
    print('To:',pdest)
    print('On:',da)
    print('Class:',cla)
    print('Reservation Type:',rety)
    print('Ticket Fair: ₹',random.randint(300, 2000))
    print('Train Number:',random.randint(100000,999999 ))



print('** Ticket Reservation **')
dest=["Hyderabad","Banglore","Mumbai","Delhi","Chennai"]
print("From:")
for i in dest:
    print(i)
sdest=input('Please enter your source location: ')
if sdest not in dest:
    print('Invalid input')
print("To:")
for i in dest:
    print(i)
pdest=input('Please enter your destination: ')
if pdest not in dest:
    print('Invalid input')
if(sdest==pdest): 
    print('Invalid destination')
else:
    res()

