#Simple Standard Calculator

from tkinter import *

import webbrowser

expression = ""

def press(num):

    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""


    except:

        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

new = 1
url = "https://youtu.be/dQw4w9WgXcQ"

def openweb():
    webbrowser.open(url,new=new)


#Window, buttons

if __name__ == "__main__":

    calculator = Tk()

    #window looks

    calculator.configure(background="grey1")

    calculator.title("Standard Calculator")

    calculator.geometry("300x400")

    equation = StringVar()

    expression_field = Entry(calculator, font=('Arial', 10),textvariable=equation, bd=0, fg="white", bg="grey1")

    expression_field.grid(columnspan=4, ipady=30, ipadx=80)

    #buttons

    #Special button

    button = Button(calculator, font='Arial', text=' ', bd=0, fg='white', bg='grey1', height=3, width=7,
    command=openweb)
    button.grid(row=5, column=1)

    #function buttons

    clear = Button(calculator, font='Arial', text='C', bd=0, fg='red', bg='salmon',
                   command=clear, height=3, width=7)
    clear.grid(row=1, column=0)

    plus = Button(calculator, font='Arial', text=' + ', bd=0, fg='white', bg='orange',
                  command=lambda: press("+"), height=3, width=7)
    plus.grid(row=1, column=3)

    minus = Button(calculator, font='Arial', text=' - ', bd=0, fg='white', bg='orange',
                  command=lambda: press("-"), height=3, width=7)
    minus.grid(row=2, column=3)

    multiply = Button(calculator, font='Arial', text=' x ', bd=0, fg='white', bg='orange',
                  command=lambda: press("*"), height=3, width=7)
    multiply.grid(row=3, column=3)

    divide = Button(calculator, font='Arial', text=' / ', bd=0, fg='white', bg='orange',
                  command=lambda: press("/"), height=3, width=7)
    divide.grid(row=4, column=3)

    equal = Button(calculator, font='Arial', text='=', bd=0, fg='white', bg='springgreen2',
                   command=equalpress, height=3, width=7)
    equal.grid(row=5, column=3)

    #decimal

    decimal = Button(calculator, font='Arial', text=' . ', bd=0, fg='white', bg='grey1',
                  command=lambda: press("."), height=3, width=7)
    decimal.grid(row=5, column=2)

    #numbers

    button0 = Button(calculator, font='Arial', text=' 0 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(0), height=3, width=7)
    button0.grid(row=5, column=0)

    button1 = Button(calculator, font='Arial', text=' 1 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(1), height=3, width=7)
    button1.grid(row=4, column=0)

    button2 = Button(calculator, font='Arial', text=' 2 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(2), height=3, width=7)
    button2.grid(row=4, column=1)

    button3 = Button(calculator, font='Arial', text=' 3 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(3), height=3, width=7)
    button3.grid(row=4, column=2)

    button4 = Button(calculator, font='Arial', text=' 4 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(4), height=3, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(calculator, font='Arial', text=' 5 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(5), height=3, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(calculator, font='Arial', text=' 6 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(6), height=3, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(calculator, font='Arial', text=' 7 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(7), height=3, width=7)
    button7.grid(row=2, column=0)

    button8 = Button(calculator, font='Arial', text=' 8 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(8), height=3, width=7)
    button8.grid(row=2, column=1)

    button9 = Button(calculator, font='Arial', text=' 9 ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(9), height=3, width=7)
    button9.grid(row=2, column=2)

    #parenthesis

    leftparen = Button(calculator, font='Arial', text=' ( ', bd=0, fg='white', bg='grey1',
                  command=lambda: press("("), height=3, width=7)
    leftparen.grid(row=1, column=1)

    rightparen = Button(calculator, font='Arial', text=' ) ', bd=0, fg='white', bg='grey1',
                  command=lambda: press(")"), height=3, width=7)
    rightparen.grid(row=1, column=2)

    calculator.mainloop()
