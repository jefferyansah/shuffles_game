import numpy as np
import random
from random import randint

#define a list of items:
base_list =['AUSTRALIA', 'PORTUGAL', 'TOGO', 'USA', 'MEXICO', 
            'CANADA', 'BOLIVIA', 'TRINIDAD', 'GHANA', 'SPAIN']

#Shuffle the list
SHUFFLE_TIMES = randint(1,10)
#use list comprehension to shuffle the base list
[random.shuffle(base_list) for i in range(SHUFFLE_TIMES)]    

#Ask the user to pick country from the list
while True:
    choose_country = input('Please Choose a Country from the list above: ').upper()
    if choose_country in base_list:
        print('You have Choosen ' + choose_country + '. The index position of ' +
        choose_country + ' in the list is ' +  str(base_list.index(choose_country)+ 1)  )
        break
    else:
        print('Ooops, the Country you have entered in not in the List')

random.shuffle(base_list) 
print('List has been Reshuffled... ')

while True:
    print('Try Guessing the New Position of '  +  choose_country + ' in the new list')
    attempt = input('Enter your Guess: ')

    if int(attempt) > base_list.index(choose_country)+ 1:
        print('Too High,  Try Again')

    elif int(attempt) < base_list.index(choose_country)+ 1:
        print('Too Low, Try Again')
    else:
        print('Yes, Got it Correct')
        break
 
    






