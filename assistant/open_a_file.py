def openi():
    file = input("open which file")
    mode = input('in which mode')

    if mode == "r":
       r = open(file,mode)
       k = r.read()
       print(k)
       r.close()
       agaion = input("do u want to run this again")
       if agaion == "yes":
           openi()

    if mode == "w":
        rt = open(file,mode)
        writing = input("what do you want to write")
        rt.write(writing)
        rt.close()
        again = input("do u want to run this again")

        if again == "yes" or again == '' :
            openi()
   # for more information visit (information to add new command.txt)