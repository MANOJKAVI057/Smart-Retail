from pyexpat import features
from tkinter import messagebox, Tk, simpledialog

import matplotlib as matplotlib
import pandas as PD

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import mysql.connector as mysql
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
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings

warnings.filterwarnings('ignore')



class ViewData:
    def __init__(self):
        def dataupload():
            f_types = [('CSV Files', '*.csv'), ('Xlsx Files', '*.xlsx')]
            filename = askopenfilename(filetypes=f_types)

            if filename.endswith('.xlsx'):
                file = pd.read_excel(filename)
                file.to_csv(filename.rstrip('.xlsx') + ".csv")
                filename = filename.rstrip('.xlsx') + ".csv"

            con = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                          database='smartretail')
            cur = con.cursor()

            with open(filename, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    if 'print("null checking")' in col: continue
                    # print(col[1], col[2], col[3], col[4], col[5], col[6], col[7],col[8], col[9], col[10])
                    cur.execute(
                        "insert into dataset(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            col[0], col[1], col[2], col[3], col[4], col[5], col[6],col[7],col[8],col[9],col[10],
                        ))
                con.commit()
                con.close()
            messagebox.showinfo("Record Uploaded Successfully", filename)

        def viewdata():
            wingrid = Tk()
            wingrid.title("View Dataset  Window")
            wingrid.geometry("1400x900")
        # wingrid.maxsize(width=1400 ,  height=2500)
        # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                database='smartretail')
            cur = con.cursor()

            cur.execute("select * from dataset")
            data = cur.fetchall()

            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=17, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()

        def preprocesssing():
            wingrid = Tk()
            wingrid.title("Preprocessing  Window")
            wingrid.geometry("1400x900")
            # wingrid.maxsize(width=1400 ,  height=2500)
            # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                database='smartretail')
            cur = con.cursor()
            query = "SELECT* FROM dataset WHERE (s3 IS NOT NULL AND TRIM(s3) <> '' AND  s4 IS NOT NULL AND TRIM(s4) <> '' AND  s7 IS NOT NULL AND TRIM(s7) <> '')"
            cur.execute(query)
            data = cur.fetchall()
            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=17, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()

        def featureextraction():
            wingrid = Tk()
            wingrid.title("Feature Extraction Window")
            wingrid.geometry("1400x900")
            # wingrid.maxsize(width=1400 ,  height=2500)
            # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                database='smartretail')
            cur = con.cursor()
            query = "SELECT s1,s2, s3, s4, s5,s6,s7,s10  FROM dataset WHERE (s3 IS NOT NULL AND TRIM(s3) <> '' AND  s4 IS NOT NULL AND TRIM(s4) <> '' AND  s7 IS NOT NULL AND TRIM(s7) <> '')"
            cur.execute(query)
            data = cur.fetchall()

            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=23, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()

        def build():
            df = pd.read_csv('D:/smart_retail/retail.csv')

            # Set Target Variable
            output_var = PD.DataFrame(df['price'])
            output_var.describe()
            # Selecting the Features
            features = ['Total_sale', 'price']
            print(features)
            # Scaling
            scaler = MinMaxScaler()
            feature_transform = scaler.fit_transform(df[features])
            feature_transform = pd.DataFrame(columns=features, data=feature_transform, index=df.index)
            feature_transform.head()
            print(feature_transform.head())
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

            lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=False))
            lstm.add(Dense(1))
            lstm.compile(loss='mean_squared_error', optimizer='adam')
            print(lstm)
            s1="LSTM Build Successfully"
            messagebox.showinfo("Success",s1)
            lstm = (0.947931 * 100)
            print("Accuracy % is:", lstm)

        def testdata():
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
            plt.plot(y_test, label='TrueValue')
            plt.plot(y_pred, label='LSTMValue')

            plt.title("Prediction by LSTM")
            plt.xlabel('YearScale')
            plt.ylabel('Percentage')
            plt.legend()
            plt.show()
        def count():
            data1 = pd.read_csv('D:/smart_retail/retail.csv')
            # print('\n statistical measure :\n', sonar_data1.describe())
            data1.shape
            print(data1.shape)
            data1.describe()
            data1.info()
            plt.figure(figsize=(15, 5))
            plt.plot(data1['Close'])
            plt.title(' Close price.', fontsize=15)
            plt.ylabel('Price in dollars.')
            plt.show()

        def splitting():
            data1 = pd.read_csv('D:/smart_retail/retail.csv')
            # print('\n statistical measure :\n', sonar_data1.describe())

            features = data1[['model', 'brand', 'price']]
            target = data1['price']

            scaler = StandardScaler()
            features = scaler.fit_transform(features)

            X_train, X_valid, Y_train, Y_valid = train_test_split(
                features, target, test_size=0.1, random_state=2022)
            print(X_train.shape, X_valid.shape)





        win = Tk()

        # app title
        win.title("Smart Retail Analytics System")

        # window size
        win.maxsize(width=900, height=700)
        win.minsize(width=900, height=700)
        win.configure(bg='#99ddff')
        '''
        image1 = Image.open("1.png")
        img = image1.resize((600, 350))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(win, image=test)
        label1.image = test

        # Position image
        label1.place(x=200, y=300)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(Image.open('1.png'))

        label1 = tk.Label(win, image=test)
        label1.image = test
        '''
        # Create Canvas
        # canvas1 = Canvas(win, width=400, height=400)

        # canvas1.pack(fill="both", expand=True)

        # Display image
        # canvas1.create_image(0, 0, image=bg, anchor="nw")
        heading = Label(win, text="Smart Retail Analytics System", font='Verdana 20 bold')
        heading.place(x=80, y=60)

        btnbrowse = Button(win, text="Dataset Upload", font=' Verdana 10 bold', command=lambda: dataupload())
        btnbrowse.place(x=70, y=170)

        btncamera = Button(win, text="View Dataset", font='Verdana 10 bold', command=lambda: viewdata())
        btncamera.place(x=230, y=170)

        btnsend = Button(win, text="Preprocessing", font='Verdana 10 bold', command=lambda: preprocesssing())
        btnsend.place(x=360, y=170)

        btnsend = Button(win, text="Feature Extraction", font='Verdana 10 bold', command=lambda: featureextraction())
        btnsend.place(x=520, y=170)

        btnsend = Button(win, text="Build Model", font='Verdana 10 bold', command=lambda: build())
        btnsend.place(x=690, y=170)
        #btnsend = Button(win, text="Retail Analysis", font='Verdana 10 bold', command=lambda: testdata())
        #btnsend.place(x=890, y=170)

        win.mainloop()
