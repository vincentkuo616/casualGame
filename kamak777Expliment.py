# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:25:59 2022

@author: vincentkuo
"""

import random
import time

tem=random.randrange(1,9)

print('Ready ~~~  Start!!')
time.sleep(1)

#for i in range(20):
#    print(('﹍--﹉--﹍--'+'﹍--﹉'*i)[-20+i:])
#    time.sleep(0.1)
#
#for i in range(8):
#    print(str(tem)+'   '+str(random.randrange(1,9))+'   '+str(random.randrange(1,9)))
#    print(str(random.randrange(1,9))+'   '+str(random.randrange(1,9))+'   '+str(random.randrange(1,9)))
#    print(str(random.randrange(1,9))+'   '+str(random.randrange(1,9))+'   '+str(random.randrange(1,9)))
#    print("-------------------------------------------------")

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
upperthaneight = 0

#for i in range(10000):
#    
#    num = 0
#    strTemp=[]
#    
#    for j in range(8):
#        a = str(tem)
#        b = str(random.randrange(1,9))
#        c = str(random.randrange(1,9))
#        d = str(random.randrange(1,9))
#        e = str(random.randrange(1,9))
#        f = str(random.randrange(1,9))
#        g = str(random.randrange(1,9))
#        h = str(random.randrange(1,9))
#        i = str(random.randrange(1,9))
#        strTemp.append([a,b,c,d,e,f,g,h,i])
#        
#        if((a==b and b==c)):
#            num+=1
#        if((d==e and e==f)):
#            num+=1
#        if((g==h and h==i)):
#            num+=1
#        if((a==d and d==g)):
#            num+=1
#        if((b==e and e==h)):
#            num+=1
#        if((c==f and f==i)):
#            num+=1
#        if((a==e and e==i)):
#            num+=1
#        if((c==e and e==g)):
#            num+=1
#    if(num==0):
#        zero+=1
#    elif(num==1):
#        one+=1
#    elif(num==2):
#        two+=1
#    elif(num==3):
#        three+=1
#    elif(num==4):
#        four+=1
#    elif(num==5):
#        five+=1
#    elif(num==6):
#        six+=1
#    elif(num==7):
#        seven+=1
#    elif(num==8):
#        eight+=1
#    else:
#        upperthaneight+=1
#    if(num>=8):
#        for i in range(8):
#            
#            print(strTemp[i][0]+"   "+strTemp[i][1]+"   "+strTemp[i][2])
#            print(strTemp[i][3]+"   "+strTemp[i][4]+"   "+strTemp[i][5])
#            print(strTemp[i][6]+"   "+strTemp[i][7]+"   "+strTemp[i][8])
#            print("......")
#        print("-------------------------------------")
#
#print('0:'+str(zero)+" "+str(round(zero*100/10000,1))+"%")
#print('1:'+str(one)+" "+str(round(one*100/10000,1))+"%")
#print('2:'+str(two)+" "+str(round(two*100/10000,1))+"%")
#print('3:'+str(three)+" "+str(round(three*100/10000,1))+"%")
#print('4:'+str(four)+" "+str(round(four*100/10000,1))+"%")
#print('5:'+str(five)+" "+str(round(five*100/10000,1))+"%")
#print('6:'+str(six)+" "+str(round(six*100/10000,1))+"%")
#print('7:'+str(seven)+" "+str(round(seven*100/10000,1))+"%")
#print('8:'+str(eight)+" "+str(round(eight*100/10000,1))+"%")
#print('>8:'+str(upperthaneight)+" "+str(round(upperthaneight*100/10000,1))+"%")

time = 0
num = 0
while(num<10):
    
    num = 0
    strTemp=[]
    
    for j in range(8):
        a = str(tem)
        b = str(random.randrange(1,9))
        c = str(random.randrange(1,9))
        d = str(random.randrange(1,9))
        e = str(random.randrange(1,9))
        f = str(random.randrange(1,9))
        g = str(random.randrange(1,9))
        h = str(random.randrange(1,9))
        i = str(random.randrange(1,9))
        strTemp.append([a,b,c,d,e,f,g,h,i])
        
        if((a==b and b==c)):
            num+=1
        if((d==e and e==f)):
            num+=1
        if((g==h and h==i)):
            num+=1
        if((a==d and d==g)):
            num+=1
        if((b==e and e==h)):
            num+=1
        if((c==f and f==i)):
            num+=1
        if((a==e and e==i)):
            num+=1
        if((c==e and e==g)):
            num+=1
    if(num==0):
        zero+=1
    elif(num==1):
        one+=1
    elif(num==2):
        two+=1
    elif(num==3):
        three+=1
    elif(num==4):
        four+=1
    elif(num==5):
        five+=1
    elif(num==6):
        six+=1
    elif(num==7):
        seven+=1
    elif(num==8):
        eight+=1
    else:
        upperthaneight+=1
    if(num>8):
        for i in range(8):
            
            print(strTemp[i][0]+"   "+strTemp[i][1]+"   "+strTemp[i][2])
            print(strTemp[i][3]+"   "+strTemp[i][4]+"   "+strTemp[i][5])
            print(strTemp[i][6]+"   "+strTemp[i][7]+"   "+strTemp[i][8])
            print("......")
        print("-------------------------------------")
    time+=1

print('0:'+str(zero)+" "+str(round(zero*100/time,1))+"%")
print('1:'+str(one)+" "+str(round(one*100/time,1))+"%")
print('2:'+str(two)+" "+str(round(two*100/time,1))+"%")
print('3:'+str(three)+" "+str(round(three*100/time,1))+"%")
print('4:'+str(four)+" "+str(round(four*100/time,1))+"%")
print('5:'+str(five)+" "+str(round(five*100/time,1))+"%")
print('6:'+str(six)+" "+str(round(six*100/time,1))+"%")
print('7:'+str(seven)+" "+str(round(seven*100/time,1))+"%")
print('8:'+str(eight)+" "+str(round(eight*100/time,1))+"%")
print('>8:'+str(upperthaneight)+" "+str(round(upperthaneight*100/time,1))+"%")
print('Time :'+str(time))
print(num)