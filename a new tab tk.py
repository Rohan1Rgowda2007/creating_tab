import tkinter

window = tkinter.Tk ()
window.title("home page")
window.geometry("300x300")
fun = ''' but you cannot resize this :(
         because it is a exernal window'''

def extra_window  ():
     window1 = tkinter.Tk()
     window1.title("External page")
     window1.geometry("400x500")
     window1.resizable('false','false')
     lab = tkinter.Label(window1,text = fun ) .pack()


button = tkinter.Button(window,text = "New tab",command = extra_window).pack()
lab = tkinter.Label(window,text = "press 'NEW WINDOW' to have a new window ").pack()

window.mainloop()