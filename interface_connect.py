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
                            if clicked_projects.get() == "HRS H2M" :
                                if clicked.get() == "BPCS/PSD" :
                                    if df['H2M'][i] == "YES" :
                                        if df['NAME'][i].find("CMD", 0, 3) != -1 :
                                            if df['DataType'][i] == "REAL" :
                                                WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, CMD)
                                            elif df['DataType'][i] == "BOOL" :
                                                WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, CMD_V)
                                
                                elif clicked.get() == "ESD" :
                                    if df['PLC'][i] == 'ESD' :
                                        if df['Address Byte_OPC NODE'][i].find("SIMUL") != -1 :
                                            temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
                                            if df['DataType'][i] == 'BOOL' :
                                                    dv = ua.DataValue(ua.Variant(CMD_V, ua.VariantType.Boolean))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)

                                            elif df['DataType'][i] == 'INT' :
                                                    dv = ua.DataValue(ua.Variant(int(CMD), ua.VariantType.Int16))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)

                                            elif df['DataType'][i] == 'REAL' :
                                                    dv = ua.DataValue(ua.Variant(CMD, ua.VariantType.Float))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)
                                            print(i, temp_var, "==========>" , temp_var.get_value())
                            
                            elif clicked_projects.get() == "HRS IP1" :
                                if clicked.get() == "BPCS/PSD" :
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
                            if clicked_projects.get() == "HRS H2M" :
                                if clicked.get() == "BPCS/PSD" :
                                    if df['H2M'][i] == "YES" :
                                        if df['NAME'][i].find("CMD", 0, 3) != -1 :
                                            if df['DataType'][i] == "REAL" :
                                                WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, CMD)
                                            elif df['DataType'][i] == "BOOL" :
                                                WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, CMD_V)
                                if clicked.get() == "ESD" :
                                    if df['PLC'][i] == 'ESD' :
                                        if df['Address Byte_OPC NODE'][i].find("SIMUL") != -1 :
                                            temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
                                            if df['DataType'][i] == 'BOOL' :
                                                    dv = ua.DataValue(ua.Variant(CMD_V, ua.VariantType.Boolean))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)

                                            elif df['DataType'][i] == 'INT' :
                                                    dv = ua.DataValue(ua.Variant(int(CMD), ua.VariantType.Int16))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)

                                            elif df['DataType'][i] == 'REAL' :
                                                    dv = ua.DataValue(ua.Variant(CMD, ua.VariantType.Float))
                                                    dv.ServerTimestamp = None
                                                    dv.SourceTimestamp = None
                                                    temp_var.set_value(dv)
                                            print(i, temp_var, "==========>" , temp_var.get_value())
                            

                            elif clicked_projects.get() == "HRS IP1" :
                                if df['H2M'][i] == "YES" :
                                    if df['NAME'][i].find("CMD", 0, 3) != -1 :
                                        if df['DataType'][i] == "REAL" :
                                            WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, CMD)
                                        elif df['DataType'][i] == "BOOL" :
                                            WriteDBlock(myplc,1586, int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, CMD_V)
                        if CMD == min_value : tmp = 1
            if clicked.get() == "BPCS/PSD" :     
                for i in range(len(df['NAME'])):
                    if df['NAME'][i].find("Mode", 0, 4) != -1 :
                        WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 0)
                    elif df['NAME'][i].find("CMD", 0, 3) != -1 :
                        if df['DataType'][i] == "BOOL" :
                                    WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 0)
                        if df['DataType'][i] == "REAL" :
                                    WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, 0)
            
            if clicked.get() == "ESD" :
                for i in range(len(df['NAME'])):
                    if df['PLC'][i] == 'ESD' :
                        if df['Address Byte_OPC NODE'][i].find("SIMUL") != -1 :
                            temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
                            if df['DataType'][i] == 'BOOL' :
                                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
                                dv.ServerTimestamp = None
                                dv.SourceTimestamp = None
                                temp_var.set_value(dv)

                            elif df['DataType'][i] == 'INT' :
                                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Int16))
                                dv.ServerTimestamp = None
                                dv.SourceTimestamp = None
                                temp_var.set_value(dv)

                            elif df['DataType'][i] == 'REAL' :
                                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Float))
                                dv.ServerTimestamp = None
                                dv.SourceTimestamp = None
                                temp_var.set_value(dv)
                            print(i, temp_var, "==========>" , temp_var.get_value())
            
            


#Toggle function call if the the button toggle function is pusshed
def toggle_function() :
    global myplc
    b = 0
    global var_fast_simulation
    if var_fast_simulation.get() :
        if clicked_projects.get() == "HRS H2M" :
            #set all the variables in the PLC BPCS/PSD to True
            if clicked.get() == "BPCS/PSD" :
                for i in range(len(df['NAME'])):
                    if df['H2M'][i] == "YES" :
                        if df['NAME'][i].find("Mode", 0, 4) != -1 :
                            WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                        if df['NAME'][i].find("CMD", 0, 3) != -1 :
                            if df['DataType'][i] == "BOOL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
                            if df['DataType'][i] == "REAL" :
                                WriteDBlock(myplc,1586,int(df['Address Byte_OPC NODE'][i]), int(df['Address Bit'][i]), S7WLReal, 1)
            
            #set all the variables in the PLC ESD to True
            if clicked.get() == "ESD" :
                for i in range(len(df['NAME'])):
                    if df['PLC'][i] == 'ESD' :
                        if df['Address Byte_OPC NODE'][i].find("SIMUL") != -1 :
                            temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
                            if df['DataType'][i] == 'BOOL' :
                                    dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))
                                    dv.ServerTimestamp = None
                                    dv.SourceTimestamp = None
                                    temp_var.set_value(dv)

                            elif df['DataType'][i] == 'INT' :
                                    dv = ua.DataValue(ua.Variant(1, ua.VariantType.Int16))
                                    dv.ServerTimestamp = None
                                    dv.SourceTimestamp = None
                                    temp_var.set_value(dv)

                            elif df['DataType'][i] == 'REAL' :
                                    dv = ua.DataValue(ua.Variant(1, ua.VariantType.Float))
                                    dv.ServerTimestamp = None
                                    dv.SourceTimestamp = None
                                    temp_var.set_value(dv)

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

#Rearmement function
def rearm() :
    if clicked.get() == "ESD" and clicked_projects.get() == "HRS H2M" :
        for i in range(len(df['NAME'])):
            if df['PLC'][i] == 'ESD' :
                if df['Address Byte_OPC NODE'][i].find("SIMUL") != -1 :
                    temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
                    if df['DataType'][i] == 'BOOL' :
                        if df['NAME'][i] == 'DIF_RMP_station_1' or df['NAME'][i] == 'DIF_RMP_station_2' or df['NAME'][i] == 'DIF_BP_rearm_ESD' :
                            dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
                            dv.ServerTimestamp = None
                            dv.SourceTimestamp = None
                            temp_var.set_value(dv)
                        else :
                            dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))
                            dv.ServerTimestamp = None
                            dv.SourceTimestamp = None
                            temp_var.set_value(dv)

                    elif df['DataType'][i] == 'INT' :
                        if df['NAME'][i].find("TT") != -1 :
                            dv = ua.DataValue(ua.Variant(4200, ua.VariantType.Int16))
                            dv.ServerTimestamp = None
                            dv.SourceTimestamp = None
                            temp_var.set_value(dv)

                        if df['NAME'][i].find("PT") != -1 :
                            dv = ua.DataValue(ua.Variant(27500, ua.VariantType.Int16))
                            dv.ServerTimestamp = None
                            dv.SourceTimestamp = None
                            temp_var.set_value(dv)

                        if df['NAME'][i].find("DG") != -1 :
                            dv = ua.DataValue(ua.Variant(1200, ua.VariantType.Int16))
                            dv.ServerTimestamp = None
                            dv.SourceTimestamp = None
                            temp_var.set_value(dv)

                    # elif df['DataType'][i] == 'REAL' :
                    #     dv = ua.DataValue(ua.Variant(1, ua.VariantType.Float))
                    #     dv.ServerTimestamp = None
                    #     dv.SourceTimestamp = None
                    #     temp_var.set_value(dv)

        sleep(0.5)


        temp_var = client.get_node('ns=3;s="DB_SIMUL_DIF"."DIF"."DIF_BP_rearm_ESD"')
        dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        temp_var.set_value(dv)
    print("rearm is called")
        # sleep(0.5)
        # for i in range(2386, len(df['NAME'])) :
        #     temp_var = client.get_node(df['Address Byte_OPC NODE'][i])
        #     print(i, temp_var, "==========>" , temp_var.get_value())

def unknown() :
    if clicked.get() == "ESD" and clicked_projects.get() == "HRS H2M" :
        rearm()
        global temp_var, temp_var_2, temp_var3, temp_var_4
        temp_var = client.get_node('ns=3;s="DB_SIMUL_DIF"."DIF"."DIF_HSS_non_ATEX_Elec"')
        dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        temp_var.set_value(dv)

        sleep(0.5)
        
        temp_var = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_BOUCLE_PUISSANCE"."BOUCLE_ARMEE"')
        temp_var_2 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."DOF"."DOF_MEP_station_1"')
        temp_var_3 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."DOF"."DOF_MEP_station_2"')
        temp_var_4 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."DIF"."DIF_HSS_non_ATEX_Elec"')
        
        print(temp_var.get_value(), temp_var_2.get_value(), temp_var_3.get_value(), temp_var_4.get_value())
        
        if temp_var.get_value() == False and temp_var_4.get_value() == False : # and temp_var_2.get_value() == False and temp_var_3.get_value() == False and temp_var_4.get_value() == False :
            rearm()

        temp_var = client.get_node('ns=3;s="DB_SIMUL_DIF"."DIF"."DIF_CTRL_DIF_HSS_non_ATEX_Elec"')
        dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        temp_var.set_value(dv)

        sleep(0.5)



        # temp_var = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_BOUCLE_PUISSANCE"."BOUCLE_ARMEE"')
        # if temp_var.get_value() == True :
        #     temp_var2 = client.get_node('ns=3;s="DB_SIMUL_DIF"."DIF"."DIF_CTRL_DIF_HSS_non_ATEX_Elec"')
        #     dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
        #     dv.ServerTimestamp = None
        #     dv.SourceTimestamp = None
        #     temp_var2.set_value(dv)

        sleep(5)
        temp_var = client.get_node('ns=3;s="DB_API_IHM_ETATS"."DIF"."DIF_CTRL_DIF_HSS_non_ATEX_Elec"')
        temp_var_2 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."DIF"."DIF_HSS_non_ATEX_Elec"')
        temp_var_3 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_BOUCLE_PUISSANCE"."BOUCLE_ARMEE"')
        print(temp_var.get_value(), temp_var_2.get_value(), temp_var_3.get_value())
        if temp_var.get_value() == False and temp_var_2.get_value() == False and temp_var_3.get_value() == False :
            print("IIIIII SUCCEEDED, yohoooooooooo")
        pass
#comment
def unknown_two() :
    global temp_var, temp_var_2
    if clicked.get() == "ESD" and clicked_projects.get() == "HRS H2M" :
        rearm()
        temp_var = client.get_node('ns=3;s="DB_SIMUL_AIF"."AIF"."AIF_D1_DG_H2_dispenser"')
        dv = ua.DataValue(ua.Variant(30000, ua.VariantType.Int16))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        temp_var.set_value(dv)

        sleep(0.5)

        temp_var = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_BOUCLE_PUISSANCE"."BOUCLE_ARMEE"')
        temp_var_2 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_1oo1_AIF"."AIF_D1_DG_H2_dispenser"."Q_DEFAUT_HH"')
        if temp_var.get_value() == False and temp_var_2.get_value() == True :
            rearm()

        temp_var = client.get_node('ns=3;s="DB_SIMUL_DIF"."DIF"."DIF_CTRL_AIF_D1_DG_H2_dispenser"')
        dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        temp_var.set_value(dv)

        sleep(0.5)

        temp_var = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_BOUCLE_PUISSANCE"."BOUCLE_ARMEE"')
        temp_var_2 = client.get_node('ns=3;s="DB_API_IHM_ETATS"."ETATS_1oo1_AIF"."AIF_D1_DG_H2_dispenser"."Q_DEFAUT_VOIE"')

        if temp_var.get_value() == False and temp_var_2.get_value() == True :
            print("Yoppppppppppeeeeeeeeeeeeee")

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
ESD_frame = LabelFrame(global_frame, text = "ESD", labelanchor="n", padx=40, pady=40)
ESD_frame.config(width = 665, height = 150)
rearmement = Button(ESD_frame, text="Rearmement", command=rearm, width=20)
test_steps = Button(ESD_frame, text="unknown", command=unknown, width=20)
test_steps2 = Button(ESD_frame, text="unknown2", command=unknown_two, width=20)


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
rearmement.grid(row=0, column=0, padx=10)
test_steps.grid(row=0, column=1, padx=10)
test_steps2.grid(row=0, column=2, padx=10)

frame_plc.place(x=10, y=10)
frame_buttons.place(x=300, y=10)
frame_projects.place(x=200, y=200)
projects_menu.place(x=10, y=200)
concepts_menu.place(x=10, y=375)
fast_simulation.place(x=200, y=170)
advanced_simulation.place(x=200, y=350)
ESD_frame.place(x=200, y=370)

root.mainloop()