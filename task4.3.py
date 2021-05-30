"""
Task 3
Words combination
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
string.For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine
characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
"""

import random

x = 0
while x < 5:
    text = "hello"
    words = text.split()
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        words[i] = ''.join(word)
        print(*words, end=' ')
        x = x + 1
