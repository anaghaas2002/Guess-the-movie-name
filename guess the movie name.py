# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:25:42 2022

@author: Admin
"""
import random
movies=['KGF','Mungaru male','Milana','Amrutha dhare','Kotigobba','Ranna','Moggina manasu']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(" ")
        else:
            temp.append("*")
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    for i in range(len(movie)):
        if(ref[i]==letter or ref[i]==" "):
            temp.append(ref[i])
        else:
            if(qn_list[i]=="*"):
                temp.append("*")
            else:
                temp.append(qn_list[i])
    return "".join(str(x) for x in temp)
            
            

def play():
    p1name=input("Please enter your name player 1 !!")
    p2name=input("Please enter your name player 2 !!")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            print(p1name,' your turn now')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_question=qn
            not_said=True
            while(not_said):
                letter=input("Guess the letter")
                if(is_present(letter,picked_movie)):
                    
                    modified_question=unlock(modified_question,picked_movie,letter)
                    print(modified_question)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter"))
                    if(d==1):
                        ans=input(" Your answer")
                        if(ans==picked_movie):
                            pp1=pp1+1
                            print("Your answer is correct")
                            not_said=False
                            print(p1name," Your score :",pp1)
                        else:
                            print("Wrong answer...Try again!!!")
                else:
                    print(letter,' not found')
                    
            c=int(input("Press 1 to continue or 0 to quit"))
            if(c==0):
                print(p1name," Your score is ",pp1)
                print(p2name," Your score is ",pp2)
                print("Thanks for playing")
                willing = False
                    
                    
                    
        else:
            print(p2name,' your turn now')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_question=qn
            not_said=True
            while(not_said):
                letter=input("Guess the letter")
                if(is_present(letter,picked_movie)):
                    
                    modified_question=unlock(modified_question,picked_movie,letter)
                    print(modified_question)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter"))
                    if(d==1):
                        ans=input(" Your answer")
                        if(ans==picked_movie):
                            pp2=pp2+1
                            print("Your answer is correct")
                            not_said=False
                            print(p2name," Your score :",pp2)
                        else:
                            print("Wrong answer...Try again!!!")
                else:
                    print(letter,' not found')
                    
            c=int(input("Press 1 to continue or 0 to quit"))
            if(c==0):
                print(p1name," Your score is ",pp1)
                print(p2name," Your score is ",pp2)
                print("Thanks for playing")
                willing = False
                
        turn=turn+1




play()