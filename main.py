import tkinter as tk

import helpingMethods

changer = helpingMethods.StringChanger()
isNum = True


def space_remover():
    pure_str = ""
    for i in range(len(changer.str)):
        if changer.str[i] != ' ':
            pure_str += changer.str[i]
    return pure_str


def on_click_0():
    if changer.str != "":
        changer.changer("0")
        lable.config(text=changer.str)


def on_click_1():
    changer.changer("1")
    lable.config(text=changer.str)


def on_click_2():
    changer.changer("2")
    lable.config(text=changer.str)


def on_click_3():
    changer.changer("3")
    lable.config(text=changer.str)


def on_click_4():
    changer.changer("4")
    lable.config(text=changer.str)


def on_click_5():
    changer.changer("5")
    lable.config(text=changer.str)


def on_click_6():
    changer.changer("6")
    lable.config(text=changer.str)


def on_click_7():
    changer.changer("7")
    lable.config(text=changer.str)


def on_click_8():
    changer.changer("8")
    lable.config(text=changer.str)


def on_click_9():
    changer.changer("9")
    lable.config(text=changer.str)


def on_click_plus():
    changer.changer(" + ")
    lable.config(text=changer.str)


def on_click_minus():
    changer.changer(" - ")
    lable.config(text=changer.str)


def on_click_cross():
    changer.changer(" × ")
    lable.config(text=changer.str)


def on_click_divide():
    changer.changer(" ÷ ")
    lable.config(text=changer.str)


def on_click_calculate():
    print(f"{changer.str}")
    str2 = space_remover()
    print(f"{str2}")

    boo1 = True
    num1, num2 = 0, 0
    pointer = 0
    is_sum = False
    is_minus = False
    is_multiply = False
    is_division = False
    test = ""

    for i in range(len(str2)):
        if str2[i] != '+' and str2[i] != '-' and str2[i] != '×' and str2[i] != '÷':
            test += str2[i]
        else:
            if str2[i] == '+':
                is_sum = True
            if str2[i] == '-':
                is_minus = True
            if str2[i] == '×':
                is_multiply = True
            if str2[i] == '÷':
                is_division = True
            if boo1:
                print(f"{test}")
                num1 = int(test)
                boo1 = False
                test = ""

    # اگر بعد از حلقه یک مقدار نهایی در test باشد، آن را به num2 اختصاص دهید
    if test:
        num2 = int(test)

    if is_sum:
        lable.config(text=num1+num2)
    if is_minus:
        lable.config(text=num1 - num2)
    if is_multiply:
        lable.config(text=num1 * num2)
    if is_division:
        lable.config(text=num1 / num2)

    print(f"num1: {num1}, num2: {num2}")


root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

lable = tk.Label(root, text=changer.str, font=('Calibri', 18))
lable.pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=20, pady=20)

# button = tk.Button(root, text="Click me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18), command=on_click_1)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
btn2 = tk.Button(buttonFrame, text="2", font=('Arial', 18), command=on_click_2)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)
btn3 = tk.Button(buttonFrame, text="3", font=('Arial', 18), command=on_click_3)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)
btn4 = tk.Button(buttonFrame, text="4", font=('Arial', 18), command=on_click_4)
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)
btn5 = tk.Button(buttonFrame, text="5", font=('Arial', 18), command=on_click_5)
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
btn6 = tk.Button(buttonFrame, text="6", font=('Arial', 18), command=on_click_6)
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
btn7 = tk.Button(buttonFrame, text="7", font=('Arial', 18), command=on_click_7)
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)
btn8 = tk.Button(buttonFrame, text="8", font=('Arial', 18), command=on_click_8)
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)
btn9 = tk.Button(buttonFrame, text="9", font=('Arial', 18), command=on_click_9)
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)
btn0 = tk.Button(buttonFrame, text="0", font=('Arial', 18), command=on_click_0)
btn0.grid(row=3, column=1, sticky=tk.W + tk.E)
btnPlus = tk.Button(buttonFrame, text="+", font=('Arial', 18), command=on_click_plus)
btnPlus.grid(row=3, column=0, sticky=tk.W + tk.E)
btnMinus = tk.Button(buttonFrame, text="-", font=('Arial', 18), command=on_click_minus)
btnMinus.grid(row=3, column=2, sticky=tk.W + tk.E)
btnCross = tk.Button(buttonFrame, text="×", font=('Arial', 18), command=on_click_cross)
btnCross.grid(row=4, column=0, sticky=tk.W + tk.E)
btnDivide = tk.Button(buttonFrame, text="÷", font=('Arial', 18), command=on_click_divide)
btnDivide.grid(row=4, column=1, sticky=tk.W + tk.E)
btnCalc = tk.Button(buttonFrame, text="=", font=('Arial', 18), command=on_click_calculate)
btnCalc.grid(row=4, column=2, sticky=tk.W + tk.E)
buttonFrame.pack(fill='x')

root.mainloop()
