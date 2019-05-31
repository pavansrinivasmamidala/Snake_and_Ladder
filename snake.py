from random import randint
import time

x,y= 0,0
snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}

print("Let's start the game")
p=0

print("Enter player-1 name: ")
p1 = input()

print("Enter player-2 name: ")
p2 = input()

while x < 100 and y < 100:
    if (p == 0):
        q = randint(1,6)    
        print("                                              Dice value:",q)
        x=x+q        
        print(p1," position: ",x)
        p=1
        time.sleep(1)        
        if x in snake_squares:
            print(p1," got bitten by snake and is now on: ",snake_squares[x])
            x = snake_squares[x]    
            continue           
        elif x in ladder_squares:
            print(p1," climbed a ladder and is now on: ",ladder_squares[x])
            x = ladder_squares[x]
            continue
        elif x > 99:
            print(p1," WON...!!!")
            break     
        else:
            continue
       
    else:
        q= randint(1,6)
        print("                                              Dice value:",q)
        y+=q
        print(p2," position: ",y)
        p=0
        time.sleep(1)
        if y in snake_squares:
            print(p2," got bitten by snake and is now on: ",snake_squares[y])
            y = snake_squares[y]    
            continue           
        elif y in ladder_squares:
            print(p2," climbed a ladder and is now on: ",ladder_squares[y])
            y = ladder_squares[y]
            continue
        elif y > 99:
            print(p2, "WON...!!!")
            break     
        else:
            continue
        