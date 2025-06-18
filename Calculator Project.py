from tkinter import *

root = Tk()
root.title("Calculator")
def Click(Type):
    if Type == "=":
        try:
            result = eval(input.get())
            input.delete(0, END)
            input.insert(END, result)
        except:
            input.delete(0, END)
            input.insert(END, "Error")
    elif Type == "C":
        input.delete(0, END)
    else:
        current = input.get()
        input.delete(0, END)
        input.insert(END, str(current) + str(Type))

B1 = Button(root, text="   1   ",padx=40 ,pady=20 ,command=lambda: Click(1)).grid(row=3, column=1 )
B2 = Button(root, text="   2   ",padx=40 ,pady=20 ,command=lambda: Click(2)).grid(row=3, column=2 )
B3 = Button(root, text="   3   ",padx=40 ,pady=20 ,command=lambda: Click(3)).grid(row=3, column=3 )
B4 = Button(root, text="   4   ",padx=40 ,pady=20 ,command=lambda: Click(4)).grid(row=4, column=1 )
B5 = Button(root, text="   5   ",padx=40 ,pady=20 ,command=lambda: Click(5)).grid(row=4, column=2 )
B6 = Button(root, text="   6   ",padx=40 ,pady=20 ,command=lambda: Click(6)).grid(row=4, column=3 )
B7 = Button(root, text="   7   ",padx=40 ,pady=20 ,command=lambda: Click(7)).grid(row=5, column=1 )
B8 = Button(root, text="   8   ",padx=40 ,pady=20 ,command=lambda: Click(8)).grid(row=5, column=2 )
B9 = Button(root, text="   9   ",padx=40 ,pady=20 ,command=lambda: Click(9)).grid(row=5, column=3 )
B0 = Button(root, text="   0   ",padx=40 ,pady=20 ,command=lambda: Click(0)).grid(row=6, column=1 )
BP = Button(root, text="   +   ",padx=40 ,pady=20 ,command=lambda: Click("+")).grid(row=6, column=2 )
BM = Button(root, text="   -   ",padx=40 ,pady=20 ,command=lambda: Click("-")).grid(row=6, column=3 )
BC = Button(root, text=" Clear ",padx=30 ,pady=20 ,command=lambda: Click("C")).grid(row=8, column=2 )
BD = Button(root, text="   /   ", padx=40, pady=20, command=lambda: Click("/")).grid(row=7, column=3)
BT = Button(root, text="   *   ", padx=40, pady=20, command=lambda: Click("*")).grid(row=7, column=1)
BE = Button(root, text="   =   ",padx=40 ,pady=20 ,command=lambda: Click("=")).grid(row=7, column=2 )
input = Entry(root, text="",width=17)
input.grid(row=1, column=2)

root.mainloop()
