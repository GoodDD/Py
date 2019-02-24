from tkinter import *
from tkinter import filedialog


def insertImg():
    file_name = filedialog.askopenfilename()
    if file_name == "":
        return
    lbox.insert(END, file_name)

def removeImg():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)


root = Tk()
root.geometry("500x500")


lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT, fill = BOTH, expand=True)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

b1 = Button(text="Add", command=insertImg)
b1.pack(fill=X)
b2 = Button(text="Delete", command=removeImg)
b2.pack(fill=X)


root.mainloop()
