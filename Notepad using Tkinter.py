#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter.messagebox import * 
from tkinter import Scrollbar
import os

window = Tk()
window.geometry('1000x1000')
TextArea = Text(window)
TextArea.grid(sticky = N + E + S + W)
file=None
Scroll=Scrollbar(TextArea)

window.grid_rowconfigure(0, weight=1) 
window.grid_columnconfigure(0, weight=1)

window.title("Untitled - Notepad")
menu = Menu(window)

Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)      
TextArea.config(yscrollcommand=Scroll.set)

def newfile():
    window.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)
    
def savefile():
    global file
    if file==None:
        file = filedialog.asksaveasfilename(initialfile='*.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                       ("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f = open(file,"w") 
            f.write(TextArea.get(1.0,END)) 
            f.close()
            window.title(os.path.basename(file) + " - Notepad")
    else: 
        f = open(file,"w") 
        f.write(TextArea.get(1.0,END)) 
        f.close()

def openfile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
        
def exitapp():
    window.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>") 

def paste(): 
    TextArea.event_generate("<<Paste>>") 

def about():
    showinfo("About Notepad", "Microsoft Windows Version 20H2")

new_item = Menu(menu,tearoff=0)
new_item.add_command(label='New',command=newfile)
new_item.add_command(label='Open',command=openfile)
new_item.add_command(label='Save',command=savefile)
new_item.add_separator()
new_item.add_command(label='Exit',command=exitapp)
menu.add_cascade(label='File', menu=new_item)

new_item1 = Menu(menu,tearoff=0)
new_item1.add_command(label='Cut',command=cut)
new_item1.add_command(label='Copy',command=copy)
new_item1.add_command(label='Paste',command=paste)
menu.add_cascade(label='Edit', menu=new_item1)

new_item3 = Menu(menu,tearoff=0)
new_item3.add_command(label='About Notepad',command=about)
menu.add_cascade(label='Help', menu=new_item3)

window.config(menu=menu)

window.mainloop()


# In[ ]:





# In[ ]:




