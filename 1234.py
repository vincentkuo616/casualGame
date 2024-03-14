# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:50:18 2022

@author: vincentkuo
"""

"""

It is a game . (棒打老虎 雞吃蟲)
Sticks attack Tigers. Tigers eat Chickens. Chickens eat Worms. Worms bit Sticks
And Sticks (1)  Tigers (2)  Chickens (3)  Worms (4)
==>     1 > 2 > 3 > 4 > 1

"""

import random


dictionary = {1:'Sticks棒',2:'Tigers老虎',3:'Chickens雞',4:'Worms蟲'}


num = random.randint(1,8)
if num%4==0: result = 4
else: result = num%4

you = int(input())
print(result)

while abs(you-result)!=1 and abs(you-result)!=3:
    if you-result==-1 or you-result==3:
        print('PC: ' + dictionary[result])
        print('Me: ' + dictionary[you])
        print('Win')
    elif result-you==-1 or result-you==3:
        print('PC: ' + dictionary[result])
        print('Me: ' + dictionary[you])
        print('Loss')
    else:
        print('PC: ' + dictionary[result])
        print('Me: ' + dictionary[you])
        print('平手')
    num = random.randint(1,8)
    if num%4==0: result = 4
    else: result = num%4
    
    you = int(input())
    print(result)
if you-result==-1 or you-result==3:
    print('PC: ' + dictionary[result])
    print('Me: ' + dictionary[you])
    print('Win')
elif result-you==-1 or result-you==3:
    print('PC: ' + dictionary[result])
    print('Me: ' + dictionary[you])
    print('Loss')
else:
    print('PC: ' + dictionary[result])
    print('Me: ' + dictionary[you])
    print('平手')