from tkinter import *
from tkinter import font
from tkinter import ttk  
from PIL import ImageTk, Image
import os

def call_window_Two_player():
    root.destroy()
    os.system("python game.py")
    

def call_window_One_player():
    root.destroy()
    os.system("python game_ai.py")
    

root = Tk()
root.title("Connect-4")
root.geometry("600x460")
root.configure(bg='white')
root.style = ttk.Style() 
root.style.configure('TButton', font = 
               ('calibri', 20), 
                    borderwidth = '4') 
#('clam', 'alt', 'default', 'classic')
root.style.theme_use("clam")
 
frame= Frame(root)
frame.pack()

imgpath = 'image.PNG'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas = Canvas(root,width=600,height=460)
canvas.create_image(740,250,anchor=E,image=photo)
canvas.pack(side="right")


w = Label(root,text="Connect-4",bg='white', fg='steelblue' ,font="none 24 bold")
w.place(relx = 0.1,rely=0.1)


button1 = ttk.Button(root, text="PLAYER Vs AI", width=20, command= call_window_One_player)
button1.place(relx =0.1, rely=0.3, anchor=W)

button2 = ttk.Button(root, text="PLAYER Vs PLAYER", width=20,command= call_window_Two_player)
button2.place(relx=0.1, rely=0.45, anchor=W)

button3 = ttk.Button(root, text="EXIT", width=20, command= frame.quit)
button3.place(relx=0.1, rely=0.6, anchor=W)


        
root.mainloop()
