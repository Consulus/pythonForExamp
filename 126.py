from tkinter import *

num = 0

def Sum():
    global num
    x = entry.get()
    num = num + int(x)
    output["text"]=num

def Clear():
    global num
    num = 0    
    output["text"]=num

window = Tk()
window.geometry("500x250")
entry = Entry(text="")
entry.place(x=30, y=20, width=100, height=25)
output = Message(text=0)
output.place(x=140, y=20, width=100, height=25)
buttonSum = Button(text="sum", command=Sum)
buttonSum.place(x=30, y=50, width=100, height=25)
buttonClear = Button(text="clear", command=Clear)
buttonClear.place(x=140, y=50, width=100, height=25)
window.mainloop()