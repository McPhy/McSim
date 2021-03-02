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

projects = ['HRS CNR',
            'HRS H2M',
            'HRS IP1',
            'HRS APEX',]
clicked_projects = StringVar()
clicked_projects.set('Select a project')

concepts = ['Sensors',
            'Actuators',
            'Alarms/Defaults',]
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
toggle = Button(frame_projects, text="Toggle function", command=connect_plc, width=20)
ramp = Button(frame_projects, text="Ramp function", command=disconnect_plc, width=20)
text_min_value = Entry(frame_projects)
text_max_value = Entry(frame_projects)
text_step_value = Entry(frame_projects)
fast_simulation = Checkbutton(global_frame, text = "Fast simulation")
advanced_simulation = Checkbutton(global_frame, text = "Advanced simulation")

# Entries' labels
label_var = StringVar()
label_min_value = Label( frame_projects, textvariable=label_var)
label_var.set("Min value :")

label_step_value = Label( frame_projects, textvariable=label_var)
label_var.set("Step value :")

label_max_value = Label( frame_projects, textvariable=label_var)
label_var.set("Max value :")

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
concepts_menu.place(x=10, y=300)
fast_simulation.place(x=200, y=170)
advanced_simulation.place(x=200, y=350)
unknown_frame.place(x=200, y=370)

root.mainloop()