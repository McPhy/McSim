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


#export xlsx file to dataframe
df = pd.read_excel('MCSIM APP Database.xlsx', sheet_name ='Sheet1', header=0)

#main interface interface
root = Tk()
root.title("McSim Simulation APP")          # Add Tittle to Root Window
root.iconbitmap(r'mcsimicon.ico')           # Logo Setup for Root Window
#root.geometry("400x400")

df = pd.read_excel(r'C:\Users\admin\Desktop\McSim\MCSIM APP Database.xlsx', sheet_name ='Sheet1', header=0)

#global variabals
myplc = None
client = None


#a function to connect PLCs after pressing the connect button
def connect_plc() :
    global client
    global myplc
    if clicked.get() == "BPCS/PSD" :
        myplc = snap7.client.Client()
        myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 
        print(myplc.get_connected())
        APIstatus = myplc.get_cpu_state()
        print("The Status of PLC is: " + APIstatus)
        print("\n")

    elif clicked.get() == "SIS" :
        url = "opc.tcp://192.168.0.105:4840"
        client = Client(url)
        client.connect()
        print("Client Connected")
        print('\n')

    elif clicked.get() == "ESD" :
        url = "opc.tcp://192.168.0.104:4840"
        client = Client(url)
        client.connect()
        print("Client Connected")
        print('\n')

#a function to disconnect PLCs after pressing the disconnect button
def disconnect_plc() :
    global myplc
    global client
    if clicked.get() == "BPCS/PSD" :
        if myplc.get_connected() :
            myplc.disconnect()
            print(myplc.get_connected())
            APIstatus = myplc.get_cpu_state()
            print("The Status of PLC is: " + APIstatus)
            print("\n")

    elif clicked.get() == "SIS" :
        client.disconnect()
        print("Client Disconnected")

    elif clicked.get() == "ESD" :
        client.disconnect()
        print("Client Disconnected")

#Ramp function call if the the button ramp function is pusshed
def ramp_function() :
    CMD = 0
    tmp = True
    CMD_V = False
    global var_fast_simulation
    if var_fast_simulation.get() :
        if myplc.get_connected() :
            min_value = float(text_min_value.get())
            step = float(text_step_value.get())
            max_value = float(text_max_value.get())
            range_inc = int((max_value - min_value)/step)
            CMD = min_value
            for y in range(1) :
                if CMD <= max_value and tmp == 1:
                    for x in range(0,range_inc + 1) :
                        if CMD_V == False : CMD_V = True
                        elif CMD_V == True : CMD_V = False
                        for i in range(len(df['NAME'])):
                            if df['H2M'][i] == "YES" :
                                if df['NAME'][i].find("CMD", 0, 3) != -1 :
                                    if df['DataType'][i] == "REAL" :
                                        WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, CMD)
                                    elif df['DataType'][i] == "BOOL" :
                                        WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, CMD_V)
                        if CMD == max_value : tmp = 0
                        CMD = CMD + step

                if CMD >= min_value and tmp == 0 :
                    for x in range(0,range_inc + 1) :
                        CMD = CMD - step
                        if CMD_V == False : CMD_V = True
                        elif CMD_V == True : CMD_V = False
                        for i in range(len(df['NAME'])):
                            if df['H2M'][i] == "YES" :
                                if df['NAME'][i].find("CMD", 0, 3) != -1 :
                                    if df['DataType'][i] == "REAL" :
                                        WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, CMD)
                                    elif df['DataType'][i] == "BOOL":
                                        WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit , CMD_V)
                        if CMD == min_value : tmp = 1


#Toggle function call if the the button toggle function is pusshed
def toggle_function() :
    global myplc
    b = 0
    global var_fast_simulation
    if var_fast_simulation.get() :
        if myplc.get_connected() :
            if clicked_projects.get() == "HRS H2M" :
                for i in range(len(df['NAME'])):
                    if df['H2M'][i] == "YES" :
                        if df['NAME'][i].find("Mode", 0, 4) != -1 :
                            WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                        if df['NAME'][i].find("CMD", 0, 3) != -1 :
                            if df['DataType'][i] == "BOOL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                            if df['DataType'][i] == "REAL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, 1)

            if clicked_projects.get() == "HRS IP1" :
                for i in range(len(df['NAME'])):
                    if df['IP1'][i] == "YES" :
                        if df['NAME'][i].find("Mode", 0, 4) != -1 :
                            WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                        if df['NAME'][i].find("CMD", 0, 3) != -1 :
                            if df['DataType'][i] == "BOOL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                            if df['DataType'][i] == "REAL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, 1)



def WriteDBlock(plc,DBlock,byte,bit,datatype,value):
    result = plc.read_area(areas['DB'],DBlock,byte,datatype)
    if datatype == S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype == S7WLByte or datatype == S7WLWord:
        set_int(result,0,value)
    elif datatype == S7WLReal:
        set_real(result,0,value)
    elif datatype == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['DB'],DBlock,byte,result)



#loading PLC list from dataframe into the OptionMenu
options = ['BPCS/PSD',
            'SIS',
            'ESD',
            ]
clicked = StringVar()
clicked.set(options[0])

projects = ['HRS CNR',
            'HRS H2M',
            'HRS IP1',
            'HRS APEX',
            ]
clicked_projects = StringVar()
clicked_projects.set('Select a project')

concepts = ['Sensors',
            'Actuators',
            'Alarms/Defaults',
            ]
clicked_concepts = StringVar()
clicked_concepts.set('Concepts')

#global frame that contains two subframes
global_frame = LabelFrame(root, text="McSim", labelanchor="n", padx=10, pady=10)
global_frame.config(width = 900, height = 570)
global_frame.grid(row=0)

#first subframe which contains the OptionMenu
frame_plc = LabelFrame(global_frame, text="PLCs", labelanchor="n", padx=40, pady=40)
frame_plc.config(width = 70, height = 50)
drop = OptionMenu(frame_plc, clicked, *options)
drop.config(width=20)
drop.pack(pady=10)


#second subframe which contains the buttons
frame_buttons = LabelFrame(global_frame, text="COM", labelanchor="n", padx=40, pady=40)
frame_buttons.config(width = 70, height = 50)
Connect = Button(frame_buttons, text="Connect",command=connect_plc, width=40)
Disonnect = Button(frame_buttons, text="Disonnect", command=disconnect_plc, width=40)

#Third subframe which contains the buttons
frame_projects = LabelFrame(global_frame, labelanchor="n", padx=40, pady=40)
#frame_projects.config(width = 800, height = 300)
toggle = Button(frame_projects, text="Toggle function", command=toggle_function, width=20)
ramp = Button(frame_projects, text="Ramp function", command=ramp_function, width=20)

text_min_value = Entry(frame_projects)
text_max_value = Entry(frame_projects)
text_step_value = Entry(frame_projects)
var_fast_simulation = IntVar()
fast_simulation = Checkbutton(global_frame, text = "Fast simulation", variable = var_fast_simulation)
advanced_simulation = Checkbutton(global_frame, text = "Advanced simulation")

# Entries' labels
label_var_min = StringVar()
label_var_step = StringVar()
label_var_max = StringVar()

label_min_value = Label( frame_projects, textvariable=label_var_min)
label_var_min.set("Min value :")

label_step_value = Label( frame_projects, textvariable=label_var_step)
label_var_step.set("Step value :")

label_max_value = Label( frame_projects, textvariable=label_var_max)
label_var_max.set("Max value :")

#Fourth subframe
unknown_frame = LabelFrame(global_frame, text = "unknown frame", labelanchor="n", padx=40, pady=40)
unknown_frame.config(width = 665, height = 150)

#OptionMenus
projects_menu = OptionMenu(global_frame, clicked_projects, *projects)
projects_menu.config(width=20)
concepts_menu = OptionMenu(global_frame, clicked_concepts, *concepts)
concepts_menu.config(width=20)






#positioning of widgets insid the frames
Connect.grid(row=0, column=0)
Disonnect.grid(row=1, column=0)

toggle.grid(row=0, column=1)
ramp.grid(row=1, column=1)
text_min_value.grid(row=1, column=2, padx=10)
text_step_value.grid(row=1, column=3, padx=10)
text_max_value.grid(row=1, column=4, padx=10)
label_min_value.grid(row=0, column=2, padx=10)
label_step_value.grid(row=0, column=3, padx=10)
label_max_value.grid(row=0, column=4, padx=10)

frame_plc.place(x=10, y=10)
frame_buttons.place(x=300, y=10)
frame_projects.place(x=200, y=200)
projects_menu.place(x=10, y=200)
concepts_menu.place(x=10, y=375)
fast_simulation.place(x=200, y=170)
advanced_simulation.place(x=200, y=350)
unknown_frame.place(x=200, y=370)

# projects_menu.grid(row=1, column=0)
# concepts_menu.grid(row=2, column=0)
# fast_simulation.grid(row=1, column=1)
# adnaced_simulation.grid(row=3, column=1)



# frame_plc.grid(row=0, column=0)
# frame_buttons.grid(row=0, column=1)
# frame_projects.grid(row=2, column=1)
# unknown_frame.grid(row=4, column=1, columnspan=2)

root.mainloop()