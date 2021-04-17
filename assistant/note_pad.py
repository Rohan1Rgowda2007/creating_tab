from tkinter import *

def writingpad():
    tk =  Tk()

    entryF = Entry(tk,width = 30 )
    entryF.pack(pady = 70 , padx = 40)
    entryF.place(y = 43,x = 95)

    tk.title ('creating file')
    tk.geometry('300x200')
    tk.config(bg = 'grey')

    lab1 = Label(tk,text ='File name |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
    lab1.pack()
    lab1.place(y = 40,x = 10)

    lab2 = Label(tk,text = 'Creating file...',bg = 'grey',fg = 'white',font = 'lucida 14 bold')
    lab2.pack()

    lab1 = Label(tk,text ='width         |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
    lab1.pack()
    lab1.place(y = 65,x = 10)

    lab1 = Label(tk,text ='height       |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
    lab1.pack()
    lab1.place(y = 100,x = 10)

    entryW = Entry(tk,width = 30)
    entryW.pack(pady = 70 , padx = 40)
    entryW.place(y = 70 , x = 95)

    entryl = Entry(tk,width = 30)
    entryl.pack(pady = 70 , padx = 40)
    entryl.place(y = 104, x = 95)

    tk.resizable(False,False)

    def creat():

          tk =  Tk()

          entryF = Entry(tk,width = 30 )
          entryF.pack(pady = 70 , padx = 40)
          entryF.place(y = 43,x = 95)

          tk.title ('creat a new file')
          tk.geometry('300x200')
          tk.config(bg = 'grey')

          lab1 = Label(tk,text ='File name |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
          lab1.pack()
          lab1.place(y = 40,x = 10)

          lab2 = Label(tk,text = 'Cret a new file',bg = 'grey',fg = 'white',font = 'lucida 14 bold')
          lab2.pack()

          lab1 = Label(tk,text ='width         |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
          lab1.pack()
          lab1.place(y = 65,x = 10)

          lab1 = Label(tk,text ='height       |',font = 'lucida 12 ',bg = 'grey',fg = 'white')
          lab1.pack()
          lab1.place(y = 100,x = 10)

          entryW = Entry(tk,width = 30)
          entryW.pack(pady = 70 , padx = 40)
          entryW.place(y = 70 , x = 95)

          entryl = Entry(tk,width = 30)
          entryl.pack(pady = 70 , padx = 40)
          entryl.place(y = 104, x = 95)

          buttonlogin = Button(tk, text='Creat', width=4, height=1, bg='grey', fg='white', font='lucida 12 bold',
                               command=notpad)
          buttonlogin.pack()
          buttonlogin.place(y=150, x=130)

          tk.resizable(False,False)

    def notpad():
        notpad = Tk()
        notpad.title(entryF.get())
        notpad.geometry(f'{entryl.get()}x{entryW.get()}')
        notpad.resizable(False,False)
        text = Text(notpad,width = entryW.get(),height = entryl.get())
        text.pack()
        menubar = Menu(notpad)

        def quiting():
            notpad.quit()

        file = Menu(menubar,tearoff = 0)
        menubar.add_cascade(label = 'file',menu  = file)
        file.add_command(label = 'save')
        file.add_command(label = 'Rename file')
        file.add_separator()
        file.add_command(label='Exit note pad',command = quiting)
        menubar.add_cascade(label = 'new',command = creat)
        notpad.config(menu = menubar)
        notpad.mainloop()

    buttonlogin = Button(tk,text = 'Creat',width = 4,height = 1,bg = 'grey',fg = 'white',font= 'lucida 12 bold',command = notpad)
    buttonlogin.pack()
    buttonlogin.place(y = 150,x = 130)


    tk.mainloop()

   # for more information visit (information to add new command.txt)