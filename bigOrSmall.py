# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:03:36 2022

@author: vincentkuo
"""

import random

tem=random.randrange(1,14)

print(tem)
time = 0
while True:
    print("下個數字大於它 或小於它")
    input_s=input()
    
    nextnum = random.randrange(1,14)
    while tem==nextnum:
        nextnum = random.randrange(1,14)
    if input_s=="B" or input_s=="b" or input_s=="Big" or input_s=="big" or input_s=="大":
        if nextnum>tem:
            print("The number is "+str(nextnum)+" Correct !")
            tem=nextnum
            time+=1
        else:
            print("The number is "+str(nextnum)+" Wrong !!")
            print("過"+str(time)+"關")
            break
    elif input_s=="S" or input_s=="s" or input_s=="Small" or input_s=="small" or input_s=="小":
        if nextnum<tem:
            print("The number is "+str(nextnum)+" Correct !")
            tem=nextnum
            time+=1
        else:
            print("The number is "+str(nextnum)+" Wrong !!")
            print("過"+str(time)+"關")
            break