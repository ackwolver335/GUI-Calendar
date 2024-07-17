import tkinter as tk 
import calendar as cd 
import tkinter.messagebox as mg

w1 =  tk.Tk()
w1.title('Calendar Generator')
w1.geometry('550x600')
w1.resizable(False,False)

frm1 = tk.Frame(w1)
frm1.pack()

lb1 = tk.Label(frm1,text = 'Calendar Generator',font = ('Fira Code',12,'bold'))
lb1.pack(padx = 2,pady = 3)

lb2 = tk.Label(frm1,text = 'Provide Year of Calendar',font = ('Fira Code',8))
lb2.pack(padx = 3,pady = 5)

e1 = tk.Entry(frm1)
e1.pack(padx = 2,pady = 3)

def method1():
    yoc = int(e1.get())
    caldr1 = cd.calendar(yoc)

    lb3.config(text = caldr1,font = "Consolas 8 bold")

btn1 = tk.Button(w1,text = 'Generate Calendar',font = ('Fira Code',10,'bold'),command = method1)
btn1.pack()

lb3 = tk.Label(w1,text = 'Calendar Generated')
lb3.pack(padx = 5)

w1.mainloop()