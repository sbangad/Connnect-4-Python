from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image

def call_game():
    os.system("python game.py")

root = Tk()
root.title("Connect-4")
root.geometry("400x150")
root.configure(bg='white')

root.style = ttk.Style() 
root.style.configure('TButton', font = ('calibri', 20),borderwidth = '4') 
#('clam', 'alt', 'default', 'classic')
root.style.theme_use("clam")
    
frame= Frame(root)
frame.pack()

imgpath = 'image.PNG'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas = Canvas(root,width=400,height=150)
canvas.create_image(535,200,anchor=E,image=photo)
canvas.pack(side="right")

button1 = ttk.Button(root, text="Play Again", width=18, command=call_game)
button1.place(relx =0.15, rely=0.4, anchor=W)

button2 = ttk.Button(root, text="Exit", width=18, command= frame.quit)
button2.place(relx=0.55, rely=0.4, anchor=W)

        
root.mainloop()


# from tkinter import *
# from tkinter.ttk import * 
  
# root = Tk() 
# root.geometry('500x500') 
  
# style = Style() 
# style.configure('TButton', font = 
#                ('calibri', 20, 'bold'), 
#                     borderwidth = '4') 
  
# # Changes will be reflected 
# # by the movement of mouse. 

# # button 1 
# btn1 = Button(root, text = 'Quit !', command = root.destroy) 
# btn1.grid(row = 0, column = 3, padx = 100) 
  
# # button 2 
# btn2 = Button(root, text = 'Click me !', command = None) 
# btn2.grid(row = 1, column = 3, pady = 10, padx = 100) 
  
# root.mainloop() 
