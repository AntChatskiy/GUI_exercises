from tkinter import *


root = Tk()
btn = Button(master=root, text="Dank memes here", command=lambda: hello())
lab = Label(master=root, text="down here, honey")
ent = Entry(master=root)
btn.pack(side=BOTTOM)
lab.pack()
ent.pack(side=RIGHT)

def hello():
    name = ent.get()
    lab.config(text="hello, {}".format(name))
    btn.config(bg = "green", fg = "red")
root.mainloop()
