# -*- coding: utf-8 -*-
"""Advance practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q1X6D9fy1IUD_34czBjs8XtF2HkIFREr
"""

print('Welcome to my Work')



#Create a string that says Hello, World!
greeting="Hello, world"
print(greeting)
#Extract the word "World" and replace it with the user’s first name (ask for their first name).
first_name=input("What is your first name:")
print(first_name)
greeting1=greeting.replace("World", first_name)
print(greeting1)
#Show the modified greeting to the user

first_name=input("What is your first name:")
greeting1=greeting.replace("World", first_name)
print(greeting1)

# Define the greeting string
greeting = "Hello, World!"

# Ask the user for input
first_name = input("What is your first name: ")

# Replace "World" with the user's first name
greeting1 = greeting.replace("World", first_name)

# Print the updated greeting
print(greeting1)

#Combine the user's first and last name (ask for both separately) using a formatted string to introduce the character fully.
greeting="Hello,World!"
#Ask the user First name as input
first_name=input("What is your first name: ")
#Ask the user last name as input
last_name=input("What is your last name: ")
#Replace the full string with combined first and last name.
new_greeting=f"hello,{first_name}{last_name}!"
#Print the Final result.
print(new_greeting)



#Ask the user to choose two numbers. These numbers will determine the character's strength and intelligence.
#Perform basic arithmetic operations (addition for strength, multiplication for intelligence) and display the results.
#Ask the user to input their numbers.
numb1=int(input("Choose any number:"))
numb2=int(input("Choose any number:"))
#Addition of Numbers
addition1=numb1+numb2
print(addition1, "Strength of these numbers")
addition2=numb1*numb2
print(addition2)

#Subtraction
subtraction1=numb1-numb2
print(subtraction1)

#Welcome to the Lahore Bazaar Mystery Box Game!
"""Ali, in front of you are 5 boxes with surprises. Some have prizes, others have puzzles, and some are empty. You can open up to three.
Which box would you like to open first? (Pick a number from 1 to 5) [User chooses box number 3]
Here's a puzzle! Solve it to win a prize: What is the national flower of Pakistan? [User types "Jasmine"]
Correct! You win a small Jasmine plant!
Do you want to open another box? (yes/no) [User chooses "no"]
Thanks for playing at Lahore Bazaar, Ali! You take home a small Jasmine plant. Come play again!"""

# CODE HERE
#Number of boxes
num_boxes=input()
print("This is puzzle , Please answer me this question?")
player=input()
print("National flower of pakistan")
player=input()
print("You win small jasmine plant!")
print("Do you want to play another game?")
player=input()
print("Thanks for playing at lahore bazaar , Ali ")

