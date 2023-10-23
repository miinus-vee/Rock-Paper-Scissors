# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:16:42 2023

@author: manasvi
"""

def rps(choice1,choice2,bit1,bit2):
    
    choice1= int(choice1[bit1]) % 3
    choice2= int(choice2[bit2]) % 3
    if (player1[choice1]==player2[choice2]):
        print("DRAW")
    elif (player1[choice1]=="rock" and player2[choice2]=="scissors"):
        print("Player 1 wins")
    elif (player1[choice1]=="rock" and player2[choice2]=="paper"):
        print("Player 2 wins")
    elif (player1[choice1]=="paper" and player2[choice2]=="scissors"):
        print("Player 2 wins")
    elif (player1[choice1]=="paper" and player2[choice2]=="rock"):
        print("Player 1 wins")
    elif (player1[choice1]=="scissors" and player2[choice2]=="paper"):
        print("Player 1 wins")
    elif (player1[choice1]=="scissors" and player2[choice2]=="rock"):
        print("Player 2 wins")
    
    
    


    
player1 = {0:"rock",1:"paper",2:"scissors"}
player2 = {0:"rock",1:"paper",2:"scissors"}
while True:
    choice1=(input())
    choice2=(input())
    bit1=int(input())
    bit2=int(input())
    rps(choice1,choice2,bit1,bit2)
    ch=input("y/n")
    if (ch=="n"):
        break