from tkinter import *

window = Tk()
window.title("String concat")
window.geometry("500x200")

def Add():
    string = entry.get()
    output["text"] = string
    
def Clear():
    output["text"] = ""

entry = Entry(text = "")
entry.place(x=20, y=30, width=200, height=30)

output = Message(text="")
output.place(x=230, y=30, width=200, height=30)
output["bg"] = "white"

btnAdd = Button(text="add", command=Add)
btnAdd.place(x=20, y=70, width=200, height=30)

btnClear = Button(text="clear", command=Clear)
btnClear.place(x=230, y=70, width=200, height=30)

window.mainloop()