
def leapyear():

    year = int(input('Enter a year:'))

    
    if (year % 400) == 00 or (year % 4) == 0:
        print("it is a leap year")

    else:
         print('it is not a leap year')

    again = input('do again')

    if again == "exit":
        print('exited sucessfully')

    if again == "" or again == "yes"    :
        leapyear()

    # for more information visit (information to add new command.txt)