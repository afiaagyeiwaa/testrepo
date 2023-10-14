#!/usr/bin/env python3
"""
Created on Sun Oct  1 18:30:51 2023

@author: afiadarkoasante
"""
def main():
    number  = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n 
        

def meow(n):
    for i in range(n):
        print("meow")