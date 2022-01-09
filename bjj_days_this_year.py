#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:36:06 2021

@author: paul
"""

import numpy as np
from datetime import datetime
from tkinter import *

try:
    days_this_year = np.genfromtxt(fname='./bjj_days_this_year.txt')

except OSError:
    open('./bjj_days_this_year.txt', "w+")
    days_this_year = np.genfromtxt(fname='./bjj_days_this_year.txt')

def submit():
    days_this_week = nome.get()
    days_this_week = np.array([[days_this_week, datetime.today()]])
    with open('./bjj_days_this_year.txt', "ab") as f:
        np.savetxt(f, days_this_week, fmt='%s')    
    master.destroy()
    
master = Tk() 
master.title('Number of jiujitsu classes in 2022')
Label(master, text="How many classes of jiujitsu did you attend this week? ").grid(row=0)  
nome = StringVar()
e1 = Entry(master, textvariable=nome) 
e1.grid(row=0, column=1) 

e2=Button(master,text = 'Submit', command = submit) 
e2.grid(row=1, column=1) 


if days_this_year.size ==0:
    total = 0
if days_this_year.size==3:
    total = days_this_year[0]
if days_this_year.size!=0 and days_this_year.size!=3:
    total = np.sum(days_this_year, axis=0)[0] 


Label(master, text=" So far you have attended "+str(int(total))+" classes in "+str(datetime.now().timetuple().tm_yday)+" days this year. ").grid(row=2)  
#Label(master, text="("+str(np.round(100*total/datetime.now().timetuple().tm_yday,2))+" percent)").grid(row=3)
Label(master, text="( Goal is 200 classes )").grid(row=3)
Label(master, text="").grid(row=4)

mainloop() 




  