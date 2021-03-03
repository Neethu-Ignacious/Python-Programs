#!/usr/bin/env python
# coding: utf-8

# In[50]:


from tkinter import *
import math

window = Tk()
window.title("GUI Calculator")
window.geometry('300x495')

expression=""
input_num=StringVar()

def clicked(item):
    global expression
    expression=expression+str(item)
    input_num.set(expression)
    
def clear(): 
    global expression 
    expression="" 
    input_num.set("")
    
def equal():
    global expression
    result=str(eval(expression))
    input_num.set(result)
    expression=result
    
def sq_rt():
    global expression
    result=math.sqrt(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    #input_num.set(expression)
 
def ln():
    global expression
    result=math.log(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def log():
    global expression
    result=math.log10(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def sin():
    global expression
    result=math.sin(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def cos():
    global expression
    result=math.cos(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def tan():
    global expression
    result=math.tan(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)

def sinh():
    global expression
    result=math.sin(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def cosh():
    global expression
    result=math.cos(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def tanh():
    result=math.tan(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
def pi():
    global expression
    result=math.pi
    input_num.set(result)
    expression=str(result)
    
def e():
    global expression
    result=math.e
    input_num.set(result)
    expression=str(result)
    
def exp():
    global expression
    result=math.exp(math.radians(float(inputfield.get())))
    input_num.set(result)
    expression=str(result)
    
def num_raised_to_10():
    global expression
    result=float(inputfield.get())**10
    input_num.set(result)
    expression=str(result)

def factorial():
    global expression
    result=math.factorial(float(inputfield.get()))
    input_num.set(result)
    expression=str(result)
    
    
inputframe=Frame(window,width=10,height=50)
inputframe.pack(side=TOP)

inputfield=Entry(inputframe,font=('arial',18,'bold'),textvariable=input_num,width=23,justify=RIGHT)
inputfield.grid(row=0,column=0)
inputfield.pack(ipady=10)

btnframe=Frame(window,width=200,height=200,bg="white")
btnframe.pack()
    
btn=Button(btnframe,text="acos",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:cosh())
btn.grid(column=0,row=1,padx=1,pady=1)

btn=Button(btnframe,text="asin",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:sinh())
btn.grid(column=1,row=1,padx=1,pady=1)

btn=Button(btnframe,text="atan",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:tanh())
btn.grid(column=2,row=1,padx=1,pady=1)

btn=Button(btnframe,text="mod",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("%"))
btn.grid(column=3,row=1,padx=1,pady=1)

btn=Button(btnframe,text="Clr",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clear())
btn.grid(column=4,row=1,padx=1,pady=1)

btn=Button(btnframe,text="cos",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:cos())
btn.grid(column=0,row=2,padx=1,pady=2)

btn=Button(btnframe,text="sin",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:sin())
btn.grid(column=1,row=2,padx=1,pady=2)

btn=Button(btnframe,text="tan",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:tan())
btn.grid(column=2,row=2,padx=1,pady=2)

btn=Button(btnframe,text="e",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:e())
btn.grid(column=3,row=2,padx=1,pady=2)

btn=Button(btnframe,text="ln",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:ln())
btn.grid(column=4,row=2,padx=1,pady=2)

btn=Button(btnframe,text="x^y",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("**"))
btn.grid(column=0,row=3,padx=1,pady=1)

btn=Button(btnframe,text="xroot",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:sq_rt())
btn.grid(column=1,row=3,padx=1,pady=1)

btn=Button(btnframe,text="x^10",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:num_raised_to_10())
btn.grid(column=2,row=3,padx=1,pady=1)

btn=Button(btnframe,text="log",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:log())
btn.grid(column=3,row=3,padx=1,pady=1)

btn=Button(btnframe,text="(",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("("))
btn.grid(column=4,row=3,padx=1,pady=1)

btn=Button(btnframe,text="7",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(7))
btn.grid(column=0,row=5,padx=1,pady=1)

btn=Button(btnframe,text="8",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(8))
btn.grid(column=1,row=5,padx=1,pady=1)

btn=Button(btnframe,text="9",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(9))
btn.grid(column=2,row=5,padx=1,pady=1)

btn=Button(btnframe,text="x!",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:factorial())
btn.grid(column=3,row=5,padx=1,pady=1)

btn=Button(btnframe,text=")",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(")"))
btn.grid(column=4,row=5,padx=1,pady=1)

btn=Button(btnframe,text="4",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(4))
btn.grid(column=0,row=6,padx=1,pady=1)

btn=Button(btnframe,text="5",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(5))
btn.grid(column=1,row=6,padx=1,pady=1)

btn=Button(btnframe,text="6",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(6))
btn.grid(column=2,row=6,padx=1,pady=1)

btn=Button(btnframe,text="*",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("*"))
btn.grid(column=3,row=6,padx=1,pady=1)

btn=Button(btnframe,text="/",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("/"))
btn.grid(column=4,row=6,padx=1,pady=1)

btn=Button(btnframe,text="1",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(1))
btn.grid(column=0,row=7,padx=1,pady=1)

btn=Button(btnframe,text="2",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(2))
btn.grid(column=1,row=7,padx=1,pady=1)

btn=Button(btnframe,text="3",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(3))
btn.grid(column=2,row=7,padx=1,pady=1)

btn=Button(btnframe,text="+",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("+"))
btn.grid(column=3,row=7,padx=1,pady=1)

btn=Button(btnframe,text="-",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("-"))
btn.grid(column=4,row=7,columnspan=2)

btn=Button(btnframe,text="0",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked(0))
btn.grid(column=0,row=8,padx=1,pady=1)

btn=Button(btnframe,text=".",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:clicked("."))
btn.grid(column=1,row=8,padx=1,pady=1)

btn=Button(btnframe,text="EXP",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:exp())
btn.grid(column=2,row=8,padx=1,pady=1)

btn=Button(btnframe,text="pi",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:pi())
btn.grid(column=3,row=8,padx=1,pady=1)

btn=Button(btnframe,text="=",width=5,height=2,font=('Palatino Linotype',12),relief=RAISED,command=lambda:equal())
btn.grid(column=4,row=8,padx=1,pady=1)

window.mainloop()


# In[ ]:




