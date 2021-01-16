# A PROGRAM TO SIMULATE THE DICE
import random

print("A DICE SIMULATOR ")

print("-----LETS BEGIN-----")

usr_input = input("Do you wish to roll a die (Enter y or n) ")#TAKING INPUT FROM THE USER

user_input = usr_input.lower();

while user_input == 'y': 
    random_number = random.randint(1,6)# GETTING RANDOM NUMBER
    string = str(random_number)# CONVERTING INT TO STRING
    print("You rolled a " +string)
    usr_input = input("Do you wish to roll a die (Enter y or n) ") # TO PERFORM UNTIL THE USER ASKS TO STOP
    user_input = usr_input.lower()
