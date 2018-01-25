#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月19日

@author: wangyz
'''
from Tkinter import *
from click.decorators import command

def resize(ev=None):
    label.config(font='Helvetica -%d' % scale.get())
    

top=Tk()
label=Label(top,text="hello world",font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)
scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)
quit=Button(top,text="quit",
            command=top.quit,activeforeground='white',
            activebackground='red')
quit.pack()
mainloop()
