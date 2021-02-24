from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from string import digits
import collections
import os
import snap7
from time import sleep 
import snap7.client as c 
from snap7.util import *
from snap7.snap7types import *
from opcua import *
from opcua import Client


#interface to search for xlsx file
Surf  = Tk()
Surf.withdraw()
file_path = filedialog.askopenfilename()

#export xlsx file to dataframe
df = pd.read_excel(file_path, sheet_name ='Sheet1', header=0)

#main interface interface
if file_path :
    root = Toplevel()
    root.title('MyApp')
    #root.geometry("400x400")

#global variabals
myplc = None
client = None


#a function to connect PLCs after pressing the connect button
def connect_plc() :
    for i in range (len(df['PLC'])) :
        if clicked.get() == df['PLC'][i] :  
            if df['Protocol'][i] == "Snap7" :
                global myplc
                myplc = snap7.client.Client()
                myplc.connect(df['IP Address'][i],0,2) #adress, rack et slot in server 
                print(myplc.get_connected())
                APIstatus = myplc.get_cpu_state()
                print("The Status of PLC is: " + APIstatus)
                print("\n")

            elif df['Protocol'][i] == "OPCUA" :
                global client
                url = "opc.tcp://"+df['IP Address'][i]+":4840"
                client = Client(url)
                client.connect()
                print("Client Connected")
                print('\n')

#a function to disconnect PLCs after pressing the disconnect button
def disconnect_plc() :
    global myplc
    global client
    for i in range (len(df['PLC'])) :
        if clicked.get() == df['PLC'][i] :
            if df['Protocol'][i] == "Snap7" :
                if myplc.get_connected() :
                    myplc.disconnect()
                    print(myplc.get_connected())
                    APIstatus = myplc.get_cpu_state()
                    print("The Status of PLC is: " + APIstatus)
                    print("\n")

            elif df['Protocol'][i] == "OPCUA" :
                client.disconnect()
                print("Client Disconnected")



#loading PLC list from dataframe into the OptionMenu
options = df['PLC']
clicked = StringVar()
clicked.set(options[0])

#global frame that contains two subframes
global_frame = LabelFrame(root, text="McSim", padx=10, pady=10)
global_frame.pack(padx=10, pady=10)

#first subframe which contains the OptionMenu
frame_plc = LabelFrame(global_frame, text="PLCs", padx=40, pady=40)
drop = OptionMenu(frame_plc, clicked, *options)
drop.pack(pady=10)

#second subframe which contains the buttons
frame_buttons = LabelFrame(global_frame, text="COM", padx=40, pady=40)
Connect = Button(frame_buttons, text="Connect", command=connect_plc)
Disonnect = Button(frame_buttons, text="Disonnect", command=disconnect_plc)

Connect.grid(row=0, column=0)
Disonnect.grid(row=1, column=0)

frame_plc.grid(row=0, column=0)
frame_buttons.grid(row=0, column=1)


root.mainloop()