from tkinter import *

window = Tk()
window.title("Convertor km to mile")
window.geometry("500x250")

def convertToKm():
    result = round(int(entryKm.get()) * 0.6214, 4)
    print(result)
    outputKm["text"] = result


entryKm = Entry(text = "")
entryKm.place(x=20, y=30, width=100, height=30)

km = Label(text="km = ")
km.place(x=125, y=30, width=40, height=30)

outputKm = Label(text=0)
outputKm.place(x=160, y=30, width=100, height=30)

outKm = Label(text="miles")
outKm.place(x=265, y=30, width=40, height=30)

btnKm = Button(text="convert to miles", command=convertToKm)
btnKm.place(x=310, y=30, width=100, height=30)

def convertToMl():
    result = round(int(entryMl.get()) * 1.6093, 4)
    print(result)
    outputMl["text"] = result


entryMl = Entry(text = "")
entryMl.place(x=20, y=70, width=100, height=30)

ml = Label(text="ml = ")
ml.place(x=125, y=70, width=40, height=30)

outputMl = Label(text=0)
outputMl.place(x=160, y=70, width=100, height=30)

outMl = Label(text="km")
outMl.place(x=265, y=70, width=40, height=30)

btnMl = Button(text="convert to km", command=convertToMl)
btnMl.place(x=310, y=70, width=100, height=30)

window.mainloop()