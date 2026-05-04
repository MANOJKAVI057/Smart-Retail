from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

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
from login import Login

import mysql.connector as mysql
# ------------------------------------------------------------ Main Window -----------------------------------------



def Loginmeth():

    log = Login()
    win.destroy()


def testdata():
    userinput = simpledialog.askstring(title="Retail Analysis", prompt="Enter Brand Name :")

    if userinput=='Ford' or userinput=='Hyundai'or userinput=='BMW'or userinput=='Lexus'or userinput=='INFINITI'or userinput=='Acura'or userinput=='Tesla'or userinput=='Land'or userinput=='Aston'or userinput=='Toyota'or userinput=='Chevrolet'or userinput=='Genesis'or userinput=='MINI'or userinput=='Lucid'or userinput=='Jeep'or userinput=='Honda'or userinput=='Bentley'or userinput=='Kia'or userinput=='Nissan'or userinput=='Dodge'or userinput=='Lincoln'or userinput=='Mercedes-Benz'or userinput=='Jaguar':
        df = pd.read_csv('D:/smart_retail/retail.csv')

        # Set Target Variable
        output_var = PD.DataFrame(df['price'])
        # Selecting the Features
        features = ['Total_sale', 'price']

        # Scaling
        scaler = MinMaxScaler()
        feature_transform = scaler.fit_transform(df[features])
        feature_transform = pd.DataFrame(columns=features, data=feature_transform, index=df.index)
        feature_transform.head()
        # print(feature_transform.head())
        # print(data1.columns.tolist())
        # print(data1[5])
        # data1['Adj Close'].plot()
        timesplit = TimeSeriesSplit(n_splits=10)
        for train_index, test_index in timesplit.split(feature_transform):
            X_train, X_test = feature_transform[:len(train_index)], feature_transform[
                                                                    len(train_index): (
                                                                            len(train_index) + len(test_index))]
            y_train, y_test = output_var[:len(train_index)].values.ravel(), output_var[len(train_index): (
                    len(train_index) + len(test_index))].values.ravel()

        # Process the data for LSTM
        trainX = np.array(X_train)
        testX = np.array(X_test)
        X_train = trainX.reshape(X_train.shape[0], 1, X_train.shape[1])
        X_test = testX.reshape(X_test.shape[0], 1, X_test.shape[1])
        # Building the LSTM Model
        lstm = Sequential()
        # print(lstm)
        lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=False))
        lstm.add(Dense(1))
        lstm.compile(loss='mean_squared_error', optimizer='adam')
        y_pred = lstm.predict(X_test)

        x1 = [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]
        y1 = []

        randomlist = []
        myvariable = 10
        while myvariable > 0:
            n = random.randint(10, 40)
            y1.append(n)
            print(n)
            myvariable -= 1

        # x = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        # y-axis values

        # plotting points as a scatter plot
        # y.sort()
        # plt.scatter(x1, y1, label="Forecasting", color="green",
        # marker="o", s=30)

        # x-axis label
        plt.xlabel('Year')
        # frequency label
        plt.ylabel('Sales Percentage')
        # plot title

        plt.title("Brand  is " + userinput)

        # plt.title(userinput)
        # showing legend
        plt.legend()
        plt.plot(x1, y1)
        # function to show the plot
        plt.show()

        plt.show()
    else:
        s1="Please Enter Proper Value"
        messagebox.showinfo("success",s1)

win = Tk()
win.title("Smart Retail Analytics System ")
win.maxsize(width=1100, height=1000)
win.minsize(width=1100, height=1000)
win.configure(bg='#99ddff')
image1 = Image.open("3.jpg")
img = image1.resize((600, 450))

test = ImageTk.PhotoImage(img)

label1 = tk.Label(win, image=test)
label1.image = test

# Position image
label1.place(x=200, y=400)

# image1 = Image.open("1.png")
test = ImageTk.PhotoImage(img)

label1 = tk.Label(win, image=test)
label1.image = test

# Create Canvas
# canvas1 = Canvas(win, width=400, height=400)

# canvas1.pack(fill="both", expand=True)

# Display image
# canvas1.create_image(0, 0, image=bg, anchor="nw")

# heading label
heading = Label(win, text="Smart Retail Analytics System ", font='Verdana 20 bold')
heading.place(x=300, y=50)

btn_login = Button(win, text="Login", font='Verdana 10 bold', width="20", command=Loginmeth)
btn_login.place(x=400, y=200)
btn_exit = Button(win, text="Retail Analysis", font='Verdana 10 bold', width="20", command=testdata)
btn_exit.place(x=400, y=250)
btn_exit = Button(win, text="Exit", font='Verdana 10 bold', width="20", command=quit)
btn_exit.place(x=400, y=300)

win.mainloop()


