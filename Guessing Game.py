import random
import math

x = random.randint(1, 101)
guesses = 0
turns = 10
name = input("What is your name? ")


while guesses < turns:
  guesses += 1
  
  user = int(input("Hey {}, pick a number between 1 and 100: ".format(name)))
  
  if x == user:
    print("Congratulations! You did it in {} tries!".format(guesses))
    break
  elif x > user:
    print("You guessed too low!")
    print("You have {} guesses left".format(turns - guesses))
  elif x < user:
    print("You guessed too high!")
    print("You have {} guesses left".format(turns - guesses))
