from tkinter import *
from asignar_var import *
from Yacc import comprobar
w=Tk()
w.geometry("300x600")
texto= StringVar()
text=StringVar()
respuesta=""

def imprimir(text,w):
    l8= Label(w, text=text,justify="right")
    l8.grid(row=27,column=0)

l= Label(w, text="Proyecto Lenguajes de Programación",font="Helvfont",justify="center")
l.grid(row=1,column=0)
l= Label(w, text="Java Funcional",font="Helvfont",justify="center")
l.grid(row=3,column=0)
img = PhotoImage(file="Java.png")
widget = Label(w, image=img).grid(row=5,column=0)
l1= Label(w, text="Se puede ingresar las siguientes estructuras:",justify="right")
l1.grid(row=11,column=0)
l2= Label(w, text="•ArrayList.",justify="right")
l2.grid(row=13,column=0)
l3= Label(w, text="•LinkedList.",justify="right")
l3.grid(row=15,column=0)
l4= Label(w, text="•DoubleLinkedList",justify="right")
l4.grid(row=17,column=0)
l5= Label(w, text="•Stack.",justify="right")
l5.grid(row=18,column=0)
l6= Label(w, text="•Queue.",justify="right")
l6.grid(row=19,column=0)
l7= Label(w, text="Ingrese su cadena: ",font="Helvfont",justify="right")
l7.grid(row=21,column=0)
f=Entry(w, textvar=texto)
f.grid(row=23,column=0)
b1=Button(w, text="Ingresar",command=lambda: asignar_var(comprobar(texto.get()),text))
b1.grid(row=25,column=0)
label1=Label(w,textvar=text).grid(row=29,column=0)

w.mainloop()

