from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import messagebox






root=Tk()
root.title("CLOCK")
root.resizable(width=False,height=False)
root.iconbitmap(r'C:\Users\Mizanur Rahman\Desktop\clock.ico')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)


cl=Label(root,font=("ds-digital",80),background='black',foreground='cyan')
cl.pack(anchor='center')


def time():
    string=strftime('%I:%M:%S %p \n   %d-%m-%y')
    month=strftime('%d-%m-%y')
    cl.config(text=string)
   
    
    cl.after(1000,time)
   
time()



root.mainloop()