import tkinter as tk 
import calendar as cd 
import tkinter.messagebox as mg

w1 =  tk.Tk()
w1.title('Calendar Generator')
w1.geometry('250x130')
w1.resizable(False,False)
w1.config(background = "#292826")

frm1 = tk.Frame(w1,bg = "#292826")
frm1.pack()

lb1 = tk.Label(frm1,text = 'Calendar Generator',font = ('Fira Code',10,'bold'),fg = "#F9D342",bg = "#292826")
lb1.pack(padx = 2,pady = 3)

lb2 = tk.Label(frm1,text = 'Provide Year of Calendar',font = ('Fira Code',8),fg = "#F9D342",bg = "#292826")
lb2.pack(padx = 3,pady = 5)

e1 = tk.Entry(frm1)
e1.pack(padx = 3,pady = 3)

def method1():

    # main calendar window code
    if len(e1.get()) > 4 or len(e1.get()) < 4:
        mg1 = mg.showwarning('Application Warning','Year length is not appropriate !')

    else:
        # new window for calendar
        w2 = tk.Toplevel(w1)
        w2.title('Calendar of ' + e1.get())
        w2.geometry('550x480')
        w2.config(bg = '#292826')

        # main code data
        yoc = int(e1.get())

        caldr = cd.calendar(yoc)
        lb1 = tk.Label(w2,text = caldr,font = "Consolas 8 bold",fg = "#F9D342",bg = "#292826")
        lb1.pack(padx = 2,pady = 3)

btn1 = tk.Button(w1,text = 'Generate Calendar',font = ('Fira Code',10,'bold'),command = method1,relief = 'groove',fg = "#F9D342",bg = "#292826")
btn1.pack(pady = 5)

w1.mainloop()