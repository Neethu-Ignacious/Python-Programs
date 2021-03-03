#!/usr/bin/env python
# coding: utf-8

# In[41]:


import xlrd
import base64
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Authentication")
window.geometry('350x200')
loc = ("C:/Users/Neethu/Desktop/neethu_test.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

lbl = Label(window, text="Username")
lbl.grid(column=0, row=0)
user = Entry(window,width=15)
user.focus()
user.grid(column=1, row=0)

lbl = Label(window, text="Password")
lbl.grid(column=0, row=1)
pas = Entry(window,width=15)
pas.focus()
pas.grid(column=1, row=1)

def Encode(id1,message):
    enc=[]
    for i in range(len(message)):
        key_c = message[i % len(id1)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def clicked():
    count=0
    userid=(user.get())
    cred=(pas.get())
    for i in range(sheet.nrows):
        if(sheet.cell_value(i, 0))==userid:
            value=Encode(userid,cred)
            if(sheet.cell_value(i, 1))==value:
                messagebox.showinfo('Message','Successful login')
                break
            else:
                messagebox.showwarning('Message','Wrong password.Try again')
                break
        count=count+1
        if count==5:
            messagebox.showerror('Message','Authentication failed')

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=4)

window.mainloop()
    


# In[ ]:





# In[ ]:




