"""
Rozważmy słowa x[0]x[1] · · · x[n − 1] oraz y[0]y[1] · · · y[n − 1] składające się z małych liter alfa-
betu łacińskiego. Takie dwa słowa są t-anagramem (dla t ∈ {0, . . . , n − 1}), jeśli każdej literze
pierwszego słowa można przypisać taką samą literę drugiego, znajdującą się na pozycji różniącej
się o najwyżej t, tak że każda litera drugiego słowa jest przypisana dokładnie jednej literze słowa
pierwszego.
"""

from typing import Deque
from zad1testy import runtests
#first approach O(n*t)
def check(x, y, litera, t, isUsed, n):
    for t in range(-t ,t + 1):
        if litera + t >= 0 and litera + t < n:
            if x[litera] == y[litera + t] and not isUsed[litera + t]: 
                isUsed[litera + t] = True
                return True 
    return False

def tanagramv1(x, y, t):
    n = len(x)
    isUsed = [False] * n #0 not used | 1 used previously
    for litera in range(n):
        if check(x, y, litera, t, isUsed, n) == False:
            return False
    return True

from collections import deque
#second aproach O(n) 
def tanagram(x, y, t):
    n = len(x)
    litery = [deque() for _ in range(26)] #creating queue for each letter
    for i in range(n):
        litery[ord(x[i])-ord('a')].append(i) #adding to correct buckets idx of actuall letter
    for i in range(n):
        tmp = litery[ord(y[i])-ord('a')].popleft()
        if  abs(tmp - i) > t: #checking if letters are in correct range
            return False
    return True

runtests( tanagram )