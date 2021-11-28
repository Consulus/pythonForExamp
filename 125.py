from tkinter import *
import random


def Roll():
    result = random.randint(1,6)
    output["text"] = str(result)

window = Tk()
window.title("Bone attack")
window.geometry("500x250")

button = Button(text = "roll the bone", command=Roll)
button.place(x = 30, y = 20, width=100, height=25)
output = Message(text="")
output.place(x = 30, y = 50, width=100, height=25)
window.mainloop()