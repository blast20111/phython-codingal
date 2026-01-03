from tkinter import *
from datetime import date
window=Tk()
window.title('multiply numbers')
window.geometry('400x300')
lbl=Label(text="hey there!",fg="blue",bg="white",height=1,width=300)
name_lbl1=Label(text="enter your first number",fg="blue",bg="white")
name_entry1=Entry()
name_lbl2=Label(text="enter your second number",fg="blue",bg="white")
name_entry2=Entry()
def display():
    num1=int(name_entry1.get())
    num2=int(name_entry2.get())
    result=num1*num2
    product="the product is "+str(result)
    text_box.insert(END,product)
    
text_box=Text(height=3)
btn=Button(text="calculate",command=display,height=1,bg="black",fg="white")
lbl.pack()
name_lbl1.pack()
name_entry1.pack()
name_lbl2.pack()
name_entry2.pack()

btn.pack()
text_box.pack()
window.mainloop()