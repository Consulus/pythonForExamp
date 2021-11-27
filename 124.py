# from tkinter import *

# def Call():
#     name = entry_box.get()
#     message = f"Hello {name}"
#     output_box["text"] = message
#     output_box["bg"] = "yellow"
#     output_box["fg"] = "white"

# window = Tk()
# window.title("Welcome")
# window.geometry("500x300")

# label = Label(text = "Enter name: ", anchor="w", padx=0)
# label.place(x = 30, y = 20, width=100, height=25)
# entry_box = Entry(text = 0)
# entry_box.place(x=30, y = 50, width=100, height=25)
# output_box = Label(text = "", anchor="w", font="bold")
# output_box.place(x=30, y = 150, width=200, height=25)
# button = Button(text = "Press me", command=Call)
# button.place(x = 30, y = 80, width=100, height=25)
# window.mainloop()

from tkinter import *

def Call():
    name = entry_box.get()
    message = str("Hello " + name)
    entry_box.delete(0, END)
    entry_box.insert(0, message)
    entry_box["bg"] = "yellow"
    entry_box["fg"] = "blue"

window = Tk()
window.title("Welcome")
window.geometry("500x300")

label = Label(text = "Enter name: ", anchor="w", padx=0)
label.place(x = 30, y = 20, width=100, height=25)

entry_box = Entry(text = "")
entry_box.place(x=30, y = 50, width=200, height=25)

button = Button(text = "Press me", command=Call)
button.place(x = 30, y = 80, width=100, height=25)
window.mainloop()