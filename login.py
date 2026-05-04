from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import random
import pymysql
import numpy as np
import pandas as pd
import pandas as PD

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sb
from fileinput import filename
from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import pymysql
import pandas as pd
import csv
from csv import writer
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename

from keras import Sequential
from keras.layers import Dense, LSTM
from keras.utils import plot_model
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings

from sklearn.model_selection import train_test_split

from main import ViewData

warnings.filterwarnings("ignore")
# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# from  Landdetails import LandDet
# from viewdetails import ViewLand



class Login:
    def __init__(self):

        def checklogin():
            if useridentry.get() == "" and passwordentry.get() == "":
                messagebox.showerror("Error", "Enter User id", parent=winlogin)
            elif useridentry.get() == "Admin" and passwordentry.get() == "Admin":
                 s1="Login Successfully"
                 messagebox.showinfo("success",s1)
                 land = ViewData()
            else:
                s1 = "Login Faild"
                messagebox.showerror("success", s1)

        winlogin = Toplevel()
        winlogin.title("Login Window")
        winlogin.maxsize(width=1200, height=900)
        winlogin.minsize(width=1200, height=900)
        winlogin.configure(bg='#99ddff')
        image1 = Image.open("2.jpg")
        img = image1.resize((600, 450))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winlogin, image=test)
        label1.image = test

        # Position image
        label1.place(x=150, y=400)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winlogin, image=test)
        label1.image = test

        # Display image
        #canvas1.create_image(300, 300, image=bg, anchor="nw")
        heading = Label(winlogin, text="Smart Retail Analytics System", font='Verdana 20 bold')
        heading.place(x=250, y=50)

        # heading label
        heading = Label(winlogin, text="Login", font='Verdana 15 bold')
        heading.place(x=430, y=100)

        # form data label
        userid = Label(winlogin, text="User Name :", font='Verdana 10 bold')
        userid.place(x=300, y=160)

        # form data label
        password = Label(winlogin, text="Password :", font='Verdana 10 bold')
        password.place(x=300, y=200)

        # Entry Box
        userid = StringVar()
        password = StringVar()
        useridentry = Entry(winlogin, width=40, textvariable=userid)
        useridentry.focus()
        useridentry.place(x=400, y=160)

        passwordentry = Entry(winlogin, width=40, show='*', textvariable=password)
        passwordentry.focus()
        passwordentry.place(x=400, y=200)

        # button login and clear

        btn_login = Button(winlogin, text="Login", font='Verdana 10 bold', command=checklogin)
        btn_login.place(x=400, y=240)

        btn_exit = Button(winlogin, text="Exit", font='Verdana 10 bold', command=quit)
        btn_exit.place(x=500, y=240)

        winlogin.mainloop()
