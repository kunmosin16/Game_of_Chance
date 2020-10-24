#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("\t\t\t ********Welcome To The Game Of Stone, Paper and Scissors*********\n\n\n")
import random
time.sleep(2)
print(f"""Please enter the difficulty level of game you wanna play
            1 Beginner
            2 Intermediate
            3 Hardcore""")
lev = int(input())
def level(l):
        time.sleep(1)
        if l==1:
            print(f"Ok so you wanna play at beginner level.I hope you know the rules of game")
        elif l==2:
            print(f"Ok so you wanna play at intermediate level")
        elif l==3:
            print(f"Ok so you wanna play at Hardcore level")
        else:
            print("Please enter valid choice")
            lev = int(input())
            level(lev)
level(lev)
no_of_attempts = 1
users_point = 0
computers_point = 0
while(no_of_attempts<=10):
    lst = ["Stone","Paper","Scissors"]
    r = random.choice(lst)
    time.sleep(2)
    print(f""" Whats Your Choice
                "Stone"
                "Paper"
                "Scissors"???
                Type it!!!!!!
                
                
                (*Remember to type first letter as capital)
                
                """)
    i = input()
    
    if i==r:
        print("Loading...........................Please Wait")
        time.sleep(2)
        print("Its a tie")
        print(f"Your choice is  {i} and the computer's choice  is also {r}")
        print(f"""As both have picken same , its a draw 
                No one gets points!!!!!!!!!!!""")



    elif i=="Paper" and  r=="Stone":
        users_point=users_point+1
        print("Loading...........................Please Wait")
        time.sleep(2)
        print(f"""Hurray !!!!!!!!!!!!!!!!!!!!!!!
                  You get a Point!!
                  Because computer has choosen stone and the paper can easily wrap the stone""")
        print("You get 1 point\n")


    elif i=="Scissors" and r=="Stone":
        computers_point = computers_point + 1
        print("Loading...........................Please Wait")
        time.sleep(2)
        print(f""" Ohh NO!!! YOu lost a point!!
                   Because you chose scissors and computer had chosen stone. Hence stone broke the scissors""")
        print("You Lost this round")
        print("Computer gets 1 point\n")

    elif i=="Stone" and r=="Scissors":
         print("Loading...........................Please Wait")
         time.sleep(2)
         print(f"""Hurray !!!!!!!!!!!!!!!!!!!!!!!
                  You get a Point!!
                  Because computer has choosen scissors and the stone can easily break the stone""")
         print("You get 1 point\n")
         print("You Won this round")
         users_point = users_point +1


    elif i == "Paper" and r == "Scissors":
        print("Loading...........................Please Wait")
        time.sleep(2)
        print(f""" Ohh NO!!! YOu lost a point!!
                   Because you chose Paper and computer had chosen Scissors. Hence Scissors can easily  cut papers!""")
        print("You Lost this round")
        print("Computer gets 1 point\n")
        computers_point = computers_point + 1



    elif i == "Scissors" and r == "Paper":
         print("Loading...........................Please Wait")
         time.sleep(2)
         print(f"""Hurray !!!!!!!!!!!!!!!!!!!!!!!
                  You get a Point!!
                  Because computer has choosen Paper and the Scissors  can easily cut the papers""")
         users_point = users_point + 1
         print("You Won this round")
         print("you get 1 point\n")

    elif i == "Stone" and r == "Paper":
        print("Loading...........................Please Wait")
        time.sleep(2)
        print(f""" Ohh NO!!! YOu lost a point!!
                   Because you chose Stone and computer had chosen Paper. Hence Papers can easily  wrap stones!""")
        computers_point=computers_point+1
        print("You Lost this round")
        print("computer gets 1 point\n")

    else:
        print("Loading...........................Please Wait")
        time.sleep(2)
        print(f"""Sorry You Have Entered a Wrong Option....
                Try once again
                *Remember to type first letter as capital 
                   """)
    print(10 - no_of_attempts, "Amount of Chances You have")
    no_of_attempts = no_of_attempts + 1
    if no_of_attempts>10:
        print("game over")
print(f""" Loading Please Wait.................
                The Winner is being Decided.......""")
time.sleep(3)

    

if computers_point > users_point:
    print(f"""OHH NO !!!! 
              You Lost The Match
              Better Luck Next Time""")

if computers_point < users_point:
    print(f"""Hurray!!!!!
              You have Won The Match !!
              Congratulations!!!
              Try increasing the level and play!!!""")
if computers_point == users_point:
    print(f""" This was a really tough game!!!
                The game has been DRAW
                Try playing again and defearing the computer!!!!!!!!!!!""")
time.sleep(1)
print(f"""
 *******************POINTS TABLE
       User point is {users_point}
       Computers point is {computers_point}***************""")
print(f"""
  **********GAME OVER*********""")

