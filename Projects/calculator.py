from tkinter import *
import tkinter


def process():
    number1 = Entry.get(E1)
    number2 = Entry.get(E2)
    operator = Entry.get(E3)
    number1 = int(number1)
    number2 = int(number2)
    if operator == "+":
        answer = number1 + number2
    if operator == "-":
        answer = number1 - number2
    if operator == "*" or operator == "x" or operator == "X":
        answer = number1 * number2
    if operator == "/":
        answer = number1 / number2
    if operator == "^":
        answer = number1 ** number2
    Entry.insert(E4, 0, answer)
    print(answer)


top = tkinter.Tk()
L1 = Label(top, text="My calculator", ).grid(row=0, column=1)
L2 = Label(top, text="Number 1", ).grid(row=1, column=0)
L3 = Label(top, text="Number 2", ).grid(row=2, column=0)
L4 = Label(top, text="Operator", ).grid(row=3, column=0)
L5 = Label(top, text="Answer", ).grid(row=4, column=0)
E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)
B = Button(top, text="Submit", command=process).grid(row=5, column=1, )

top.mainloop()
