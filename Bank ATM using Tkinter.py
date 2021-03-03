#!/usr/bin/env python
# coding: utf-8

# In[49]:


from tkinter import *
import math

window = Tk()
window.title("ATM")
window.geometry('350x340')

expression=""
input_num=StringVar()
acc_bal=2000

def clicked(item):
    global expression
    expression=expression+str(item)
    input_num.set(expression)
    
def clear(): 
    global expression 
    expression="" 
    input_num.set("")
    
def deposit():
    global acc_bal
    global expression
    result=float(inputfield.get())
    acc_bal=acc_bal+result
    expression="Rs "+str(result)+" Depostited"
    input_num.set(expression)
    
def withdraw():
    global acc_bal
    global expression
    result=float(inputfield.get())
    acc_bal=acc_bal-result
    expression="Rs "+str(result)+" Withdrawn"
    input_num.set(expression)
    
def balance():
    global acc_bal
    global expression
    expression="Account balance:"+"Rs "+str(acc_bal)
    input_num.set(expression)

def exitapp():
    window.destroy()

inputframe=Frame(window,width=12,height=40)
inputframe.pack(side=TOP)

inputfield=Entry(inputframe,font=('arial',18),textvariable=input_num,width=27,justify=RIGHT)
inputfield.grid(row=0,column=0)
inputfield.pack(ipady=10)

btnframe=Frame(window,width=250,height=350,bg="grey")
btnframe.pack()


btn=Button(btnframe,text="1",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(1))
btn.grid(column=0,row=2,padx=1,pady=1)

btn=Button(btnframe,text="2",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(2))
btn.grid(column=1,row=2,padx=1,pady=1)

btn=Button(btnframe,text="3",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(3))
btn.grid(column=2,row=2,padx=1,pady=1)


btn=Button(btnframe,text="4",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(4))
btn.grid(column=0,row=3,padx=1,pady=1)

btn=Button(btnframe,text="5",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(5))
btn.grid(column=1,row=3,padx=1,pady=1)

btn=Button(btnframe,text="6",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(6))
btn.grid(column=2,row=3,padx=1,pady=1)


btn=Button(btnframe,text="7",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(7))
btn.grid(column=0,row=4,padx=1,pady=1)

btn=Button(btnframe,text="8",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(8))
btn.grid(column=1,row=4,padx=1,pady=1)

btn=Button(btnframe,text="9",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(9))
btn.grid(column=2,row=4,padx=1,pady=1)


btn=Button(btnframe,text="<-",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clear())
btn.grid(column=0,row=5,padx=1,pady=1)

btn=Button(btnframe,text="0",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(0))
btn.grid(column=1,row=5,padx=1,pady=1)

btn=Button(btnframe,text="CE",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clear())
btn.grid(column=2,row=5,padx=1,pady=1)


btn=Button(btnframe,text="Deposit",width=15,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:deposit())
btn.grid(column=5,row=2,padx=30,pady=5)

btn=Button(btnframe,text="Withdraw",width=15,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:withdraw())
btn.grid(column=5,row=3,padx=30,pady=5)

btn=Button(btnframe,text="Balance",width=15,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:balance())
btn.grid(column=5,row=4,padx=30,pady=5)

btn=Button(btnframe,text="Exit",width=15,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:exitapp())
btn.grid(column=5,row=5,padx=30,pady=5)

window.mainloop()


# In[ ]:





# In[ ]:




