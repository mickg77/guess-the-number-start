"""
Number Game by Michael Griffiths
21st March 2023

"""

import random
from art import logo
print(logo)

def difficulty_level():
  level=""
  while level!="easy" or level!="Easy" or level!="hard" or level!="Hard": #validates input
    level = input("Which level of difficulty do you want? Easy | Hard \n")

    if (level == "Easy" or level == "easy"):
        print("You have chosen Easy, you get 10 turns.")
        return 10 #easy is chosen and 10 returned
    elif (level == "Hard" or level == "hard"):
        print("You have chosen hard, you get 5 goes.")
        return 5 #hard is chosen and 5 returned


def checker(attempt,difficulty):
  guess = 0
  number = random.randint(1, 100)
  while (guess != number and attempt < difficulty):
      guess = int(input("Enter your guess : "))
      attempt = attempt + 1
      if (guess > number):
          print("Unlucky, too high!")
      elif (guess < number):
          print("Unlucky, too low!")
      elif (guess == number): #success
          print("Well done, you've got it!")
          break
  if attempt==difficulty: ##ran out of attempts
    print("You lose")
    print(f"The number was : {number}")

def game():
   
  attempt = 0 #set attempts to zero
  difficulty = difficulty_level() #will return 5 or 10
  checker(0, difficulty) #checks the guesses


game()