from tkinter import *
w=Tk()
w.geometry("350x400")

l= Label(w, text="Java Funcional",font="Helvfont",justify="center")
l.grid(row=0,column=1)
img = PhotoImage(file="Java.png")
widget = Label(w, image=img).grid(row=1,column=1)
l= Label(w, text="Proyecto Lenguajes de Programación",font="Helvfont",justify="center")
l.grid(row=2,column=1)

w.mainloop()
