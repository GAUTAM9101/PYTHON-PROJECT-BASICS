# A PROGRAM TO MAKE THE USER GUESS THE RANDOM NUMBER GENERATED

import random

print("A random number will be generated between 30 to 50")

rand_num = random.randint(30,50) # GENERATING RANDOM NUMBER 
input_user = int(input("Guess the random number generated (30-50) : "))
if input_user == rand_num :
    print("<<<<<< Hurray ! You guessed it right >>>>>>  ")

elif input_user > 50 or input_user < 30 : # IF INPUT ISNT IN RANGE (30-50)
            print("The number is not in the range (30-50)")

else:
    while input_user != rand_num :
        
        
        if input_user < rand_num :
            print("The number is larger ")

        elif input_user > rand_num :
            print("The number is smaller")
        input_user = int(input("Guess the random number generated (30-50) : "))
        if input_user == rand_num :
            print("<<<<<< Hurray ! You guessed it right >>>>>>  ")
