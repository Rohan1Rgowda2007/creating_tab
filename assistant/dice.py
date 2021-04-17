from random import randint

def dice():

     sh = randint(1,6)

     print(sh)

     again = input()

     if again == "" or again == 'yes':
         dice()

