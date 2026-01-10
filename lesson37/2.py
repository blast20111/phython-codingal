from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("100x100")
def msg():
    messagebox.showwarning("alert","stop! virus found")
button=Button(window,text="scan for virus",command=msg)
button.place(x=40,y=80)
window.mainloop()