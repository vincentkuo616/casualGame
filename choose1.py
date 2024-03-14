# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:27:56 2022

@author: vincentkuo
@discription: 若有配對到的則答案是它，若沒有答案是其它
"""

abcde = ['a','b','c','d','e']
ABCDE = ['A','B','C','D','E']

import random
import time

begin = time.time()

randomOne = random.sample([0,1,2,3,4],2)
randomTwo = random.sample([0,1,2,3,4],2)

one = [abcde[randomOne[0]],abcde[randomOne[1]]]
two = [ABCDE[randomTwo[0]],ABCDE[randomTwo[1]]]


''' 此方法會重複 a a b 之類的
one = random.choices(abcde,k=2)
two = random.choices(ABCDE,k=2)
'''

def getAns(a,b,c,d):
    ans = []
    if a==b.lower():
        ans.append(a)
    if c==d.lower():
        ans.append(c)
    if a!=b.lower() and c!=d.lower():
        ans = [i for i in abcde if i not in [a,b.lower(),c,d.lower()]]
    return ans

print(one[0],two[0])
print(one[1],two[1])

answer = input("The answer is ... ? ")

if answer in getAns(one[0],two[0],one[1],two[1]):
    print('Correct!! ')
    print('The answer is')
    print(getAns(one[0],two[0],one[1],two[1]))
else:
    print('Wrong!! The answer is')
    print(getAns(one[0],two[0],one[1],two[1]))