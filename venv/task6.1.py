'''
Make a program that has some sentence (a string) on input and returns a dict containing all unique words
as keys and the number of occurrences as values.
'''
#без совісті мною взятий текс пісні БАНДИ METALLICA
my_text ='''
Hey , I'm your life, I'm the one who takes you there
Hey , I'm your life, I'm the one who cares
They , they betray, I'm your only true friend now
They , they'll betray, I'm forever there
I'm your dream, make you real
I'm your eyes when you must steal
I'm your pain when you can't feel
Sad but true
I'm your dream, mind astray
I'm your eyes while you're away
I'm your pain while you repay
You know it's sad but true
Sad but true
You , you're my mask, you're my cover, my shelter
You , you're my mask, you're the one who's blamed
Do , do my work, do my dirty work, scapegoat
Do , do my deeds for you're the one who's shamed
I'm your dream, make you real
I'm your eyes when you must steal
I'm your pain when you can't feel
Sad but true
I'm your dream, mind astray
I'm your eyes while you're away
I'm your pain while you repay
You know it's sad but true
Sad but true'''
my_dict = { }
for word in my_text.split():
    my_dict[word] = my_dict.get(word, 0) + 1

print(my_dict)
