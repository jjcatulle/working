

import names
from random import randint, choice
from random import getrandbits
import random
import time
import secrets
import string
from lazyme.string import color_print


#print ("[" + (time.strftime("%H:%M:%S")) + "]" + " WELCOME TO MY MAILING INFO JIGGER     ")
#print ("[" + (time.strftime("%H:%M:%S")) + "]" + "            by Jean     ")
catchall=str(input('Enter your catchall domain: '))
print ('                  ')
address=str(input("Enter Your Street Address: "))
print ('                  ')
city=str(input("enter the name of your city: "))
print ('                  ')
zipcode=str(input('enter your 5 digit zipcode: '))
try:
   status = int(zipcode)
except ValueError:
   print("That's not valid zipcode restard the code again!")
print ('                  ')
state1=str(input('enter the 2 letter abbriviation of your state: '))
state=state1.capitalize()
try:
    status= str(state) and len(state)<3
except ValueError:
    print("please print the two letter abbriviation again")
print ('                  ')
country=str(input('UK or US: '))
print ('                  ')
area= str(input('what is your phone number area code: '))
print ('                  ')
tries=int(input('how many?: '))
print ('                  ')
#answer=input('y=address prefix, n=address suffix: ')
bot_names=str(input('cyber,astro,eve,kickmoji, bnb: '))
if bot_names=='bnb':
    shipping=str(input('what is the shipping address'))
print ('                  ')
print('        Credit Card(s) Info       ')
print ('                  ')
def nmes():
    full_names=names.get_full_name()
    
    gender = choice(['male', 'female'])
    firstname = names.get_first_name(gender=gender)
    lastname = names.get_last_name()
    email = (firstname + choice("-_.") + lastname).lower() + "".join([str(randint(0, 10)) for x in range(randint(1, 5))])+'@' + catchall

    #ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char = 3
    prefix= string.ascii_uppercase + string.digits
	
    prefix1 = ''.join(random.choice(prefix) for _ in range(char))
	

    num1=randint(100,999)
    num2=randint(1000,9999)
    '''if answer = str(y):
        print :
    if answer = str(n):
        print:
    else:
        print('that is not a valid answer, please pick y/n!!')
    print(full_names)
    '''
    address1=(prefix1+' '+address)
    address2=('apt '+str(num2))
    phone=area+'-'+str(num1)+'-'+str(num2)
    phone1=area+str(randint(2345532,9864567))
    address3=' '
    cardNumber=input('cardNumber: ')
    cardMonth=input('cardmonth: ')
    cardYear=input('cardyear(####): ')
    cardCVV=input('cardcvv: ')
    astro_file= ("astro.csv")
    eve_file=("eve.csv")
    kickmoji_file=("kickmoji.csv")
    bnb_file=("bnb.csv")
    numb=str(randint(1,100))
    cardtype='cardtype'

    
   
    astro=(firstname+','+full_names+','+phone+','+email+','+address+','+address2+','+city+','+state+','+zipcode+','+country+','+cardNumber+','+cardMonth+','+cardYear+','+cardCVV)
    astro1=(firstname+','+full_names+','+phone+','+email+','+address1+','+address3+','+city+','+state+','+zipcode+','+country+','+cardNumber+','+cardMonth+','+cardYear+','+cardCVV)
    #cyber=
    kickmoji=(numb+','+firstname+','+firstname+','+lastname+','+address3+','+address3+','+phone1+','+cardtype+','+cardNumber+','+cardCVV+','+','+cardMonth+','+cardYear+','+address+','+address2+','+address3+','+city+','+state+','+country+','+zipcode)
    eve='trial'
    bnb=(firstname+','+firstname+','+lastname+','+address+','+address2+','+','+zipcode+','+phone1+','+city+','+state)
    if bot_names=='astro':
        f = open(astro_file,'a')
        f.write(astro+ '\n')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " loading............")
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Profile successfully created............")

        print ('                  ')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " please enter your new card information............")
    elif bot_names=='eve':
        f = open(eve_file,'a')
        f.write(eve+ '\n')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " loading............")
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Profile successfully created............")

        print ('                  ')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " please enter your new card information............")

    elif bot_names=='kickmoji':
        f = open(kickmoji_file,'a')
        f.write(kickmoji+ '\n')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " loading............")
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Profile successfully created............")
        print ('                  ')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " please enter your new card information............")
        
    elif bot_names=='bnb':
        f = open(bnb_file,'a')
        f.write(kickmoji+ '\n')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " loading............")
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Profile successfully created............")
        print ('                  ')
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " please enter your new card information............")

    else:
        print ("[" + (time.strftime("%H:%M:%S")) + "]" + "we are working on a template for"+bot_names)









'''
    if answer=='y':
        
        f = open(filename,'a')

        f.write(astro1+ '\n')
        print('loading.........')

    elif answer=='n':
        
        f = open(filename,'a')

        f.write(astro+ '\n')
        print ("we're almost done......")
    else:
        print ('please choose y(yes) or n(no)')
    
    #print (email)
    #print (address+' apt'+prefix)
    '''

for i in range(tries):
    nmes()
print('   ')
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "All Profiles successfully created and saved as " + bot_names+".csv")
print('   ')
print('   ')

print ("[" + (time.strftime("%H:%M:%S")) + "]" + "          Please Donate To: ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " the Epilepsy Foundation New England ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " 335 Main St., Wilmington, MA 01887")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "              or  ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " the American Foundation for Suicide Prevention (AFSP) ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " 120 Wall St., 29th Floor, New York, NY 10005")
print('   ')
print('   ')
