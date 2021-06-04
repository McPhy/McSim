#client OPC-UA PYTHON
from opcua import *
from opcua import Client
import time
from datetime import datetime
from time import sleep
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from string import digits
import numpy as np

c = 0

url = "opc.tcp://192.168.0.104:4840"
client = Client(url)
client.connect()
print("Client Connected")
print('\n')



# dv_Tol = ua.DataValue(ua.Variant(5.3, ua.VariantType.Float))
# dv_Tol.ServerTimestamp = None
# dv_Tol.SourceTimestamp = None
# Test_node.set_value(dv_Tol)
# print("TOLERANCE :", Test_node.get_value())

# Activate = client.get_node('ns=3;s="DB_IHM_API_CMD"."SEUILS_REDUITS"."ACTIVER"')
# print (Activate)

# Test_node = client.get_node(str(df['Nodes'][23]))
# print(Test_node)
# print(df['Nodes'][23])


"""
while True:

        # Temp = client.get_node("ns=3;s=\"DB_API_IHM_ETATS\".\"DIF\".\"DIF_CTRL_AIF_D1_TT_Aval_secu_a\"")
        # print(Temp.get_value())
        # Type INT
        #dv = ua.DataValue(ua.Variant(5, ua.VariantType.Int32))
        #dv.ServerTimestamp = None
        #dv.SourceTimestamp = None
        #print(Temp.set_value(dv))
        
        # Type Bool
        # dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))
        # dv.ServerTimestamp = None
        # dv.SourceTimestamp = None
        # print(Temp.set_value(dv))

        #Type Real
        #dv = ua.DataValue(ua.Variant(2.67, ua.VariantType.Float))
        #dv.ServerTimestamp = None
        #dv.SourceTimestamp = None
        #print(Temp.set_value(dv))

 
        Activate = client.get_node('ns=3;s="DB_IHM_API_CMD"."SEUILS_REDUITS"."ACTIVER"')

        TOLERANCE = client.get_node('ns=3;s="DB_IHM_API_CMD"."SEUILS_REDUITS"."AIF_PT_In_1st_head_1oo2_TOLERANCE"')
        #Activate = client.get_node("ns=3;s=\"DB_IHM_API_CMD\".\"SEUILS_REDUITS\".\"ACTIVER\"")
        
        dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        Activate.set_value(dv)
        print(Activate.get_value())

        sleep(2)
        #Activate = client.get_node('ns=3;s="DB_IHM_API_CMD"."SEUILS_REDUITS"."ACTIVER"')
        #Activate = client.get_node("ns=3;s=\"DB_IHM_API_CMD\".\"SEUILS_REDUITS\".\"ACTIVER\"")
        #Activate = client.get_node("ns=3;s=\"DB_IHM_API_CMD\".\"SEUILS_REDUITS\".\"\"")
        dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        Activate.set_value(dv)
        print(Activate.get_value())

        i = i + 0.5

        dv_Tol = ua.DataValue(ua.Variant(i, ua.VariantType.Float))
        dv_Tol.ServerTimestamp = None
        dv_Tol.SourceTimestamp = None
        TOLERANCE.set_value(dv_Tol)
        print("TOLERANCE :", TOLERANCE.get_value())
        #print('test= ' + str(Temperature))
        #Pression = client.get_node("ns=4;s=MES_EANA_SECU_COM_AIF_PT_ST10_a")
        #PR10 = Pression.get_value()
        #print(Temperature)
        #print('PT STK 10 = ' + str(PR10))
        
        Time = datetime.now()
        print('Time :' + str(Time))
        print('\n')
        time.sleep(2)
"""