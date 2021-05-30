"""Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""
import random

str_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1):
    random.shuffle(str_1)
    print(str_1)
