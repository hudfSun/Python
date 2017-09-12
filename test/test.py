#coding:utf-8
from random import randint

num = randint(1,100)
bingo = False
while bingo == False:
    answer = input("Guess what you think?")
    if answer > num:
        print '%d too large'% answer
    if answer < num:
        print '%d too small'% answer
    if answer == num:
        print "bingo,%d is right answer" % answer
        bingo=True
        