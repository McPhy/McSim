#GUI LIB
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk

#Prints LIB
import pprint

#Data Management LIBs
import pandas as pd 
import numpy as np


#System LIBS
from datetime import datetime
from time import sleep
import os

#PATHS
KeyFile =  'X:\\McView_DataAnalysis.xlsx'


#Global Variables
global Value1
global Value1_Reg2
global NameList
global DF_DataBase
global DatabaseFiltrado
global DF_DataBase2


# Snap 7 package
import snap7
import snap7.client as c 
from snap7.util import *
from snap7.snap7types import *



# Anaconda Packages
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np 
import pandas as pd
from pandas.plotting import register_matplotlib_converters






NameList = "No Value"
Value1 = "No Value"

# GUI Settings
window = Tk()							# Application set-up
window.geometry('1000x1000')				# Window Wize Dimensions
window.title("McView Data Logging Client")		# Window Tittle Set-up
window.iconbitmap(r'statistics.ico')

 


 # ----------------------------------- Declaration of Variables -----------------------------------------------------
# Values
Y_Value1 = []
Y_Value2 = []
Y_Value3 = []
Y_Value4 = []
Y_Value5 = []
Y_Value6 = []
Y_Value7 = []
Y_Value8 = []
Y_Value9 = []
Y_Value10 = []


X_val = []

LogFolder = 'X:\\McView DataAnalysis\\'

TagName1 = 'value1'
TagName2 = 'value2'
TagName3 = 'value3'
TagName4 = 'value4'
TagName5 = 'value5'
TagName6 = 'value6'
TagName7 = 'value7'
TagName8 = 'value8'
TagName9 = 'value9'
TagName10 = 'value10'

flagValue1 = 1
flagValue2 = 1
flagValue3 = 1
flagValue4 = 1
flagValue5 = 1
flagValue6 = 1
flagValue7 = 1
flagValue8 = 1
flagValue9 = 1
flagValue10 = 1
flagValueTime = 1
Mem_Flag1 = 0
Mem_Flag2 = 0
Mem_Flag3 = 0
LOOPNumber = 0

Activation_Con = 0
ETAT = 0

#===================================================================================================================


#Functions

#Snap 7 Functions Lectura de DB del PLC "DB"
def ReadDBlock(plc,DBlock,byte,bit,datatype):
	result = plc.read_area(areas['DB'],DBlock,byte,datatype)
	if datatype == S7WLBit:
		return get_bool(result,0,bit)
	elif datatype == S7WLByte or datatype == S7WLWord:
		return get_int(result,0)
	elif datatype == S7WLReal:
		return get_real(result,0)
	elif datatype == S7WLDWord:
		return get_dword(result,0)
	else:
		return None






def CloseProgram():
	global Activation_Con
	global ETAT
	global myplc

	myplc = snap7.client.Client()
	myplc.disconnect() #adress, rack et slot in server
	print('PLC Disconected')
	Activation_Con = 0
	ETAT = 0
	print('Activ ' + str(Activation_Con))

def StartProgram():
	global Activation_Con
	global ETAT
	global myplc
	
		#--------------------------------------------- [ Snap 7 - Client Connection ] -------------------------------------------
	#Estableciendo Cliente y Conexion el Automata

	myplc = snap7.client.Client()
	myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 


	#Call Funcion para conectarse al servidor como cliente
	ETAT = myplc.get_connected()
	print('Conection Established: ' + str(ETAT))
	if ETAT == True:
		Activation_Con = 1
		print('Activ ' + str(Activation_Con))

	#Call funcion para ver estatus del PLC
	APIstatus = myplc.get_cpu_state()
	print("PLC Status: " + APIstatus)
	print("McView DataAnalysis Status: RUN")
	print("\n")




	# ----------------------------------- Declaration of Variables -----------------------------------------------------
	# Values
	Y_Value1 = []
	Y_Value2 = []
	Y_Value3 = []
	Y_Value4 = []
	Y_Value5 = []
	Y_Value6 = []
	Y_Value7 = []
	Y_Value8 = []
	Y_Value9 = []
	Y_Value10 = []


	X_val = []

	LogFolder = 'X:\\McView DataAnalysis\\'

	TagName1 = 'value1'
	TagName2 = 'value2'
	TagName3 = 'value3'
	TagName4 = 'value4'
	TagName5 = 'value5'
	TagName6 = 'value6'
	TagName7 = 'value7'
	TagName8 = 'value8'
	TagName9 = 'value9'
	TagName10 = 'value10'

	flagValue1 = 1
	flagValue2 = 1
	flagValue3 = 1
	flagValue4 = 1
	flagValue5 = 1
	flagValue6 = 1
	flagValue7 = 1
	flagValue8 = 1
	flagValue9 = 1
	flagValue10 = 1
	flagValueTime = 1


	#===================================================================================================================





	#----------------------------------------[     Void Main Cyclic      ] --------------------------------------------
	Mem_Flag1 = 0
	Mem_Flag2 = 0
	Mem_Flag3 = 0
	LOOPNumber = 0




	





	#===================================================================================================================









def loop():
	global Activation_Con
	print('Activ loop ' + str(Activation_Con))

	# Values
	global Y_Value1
	global Y_Value2
	global Y_Value3
	global Y_Value4
	global Y_Value5
	global Y_Value6
	global Y_Value7
	global Y_Value8
	global Y_Value9
	global Y_Value10


	global X_val

	LogFolder = 'X:\\McView DataAnalysis\\'

	global TagName1
	global TagName2
	global TagName3
	global TagName4
	global TagName5
	global TagName6
	global TagName7
	global TagName8
	global TagName9
	global TagName10

	global flagValue1
	global flagValue2
	global flagValue3 
	global flagValue4 
	global flagValue5
	global flagValue6
	global flagValue7
	global flagValue8
	global flagValue9
	global flagValue10
	global flagValueTime
	global Mem_Flag1
	global Mem_Flag2
	global Mem_Flag3
	global LOOPNumber
	global ETAT
	global myplc


	if Activation_Con == 1:


		if ETAT == False:
			sleep(5)
			myplc = snap7.client.Client()
			myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 
			ETAT = myplc.get_connected() 
			print(ETAT)
			Mem_Flag1 = 0
			Mem_Flag3 = 0


		if ETAT == True:

			Start_Distribution_D1 = ReadDBlock(myplc,1581,0,2,S7WLBit)		# Lectura de Dato en un DB del Plc
			
			
			###### Subrutina de la linea de Distribucion 1
			if Start_Distribution_D1 == 1 and Mem_Flag1 == 0:					# Comienzo de Distribucion de la Estacion
				print("Button Log Activated")
				print("\n")
				Mem_Flag1 = 1												# Flag de memoria para no entrar al bucle hasta terminar Distribucion

				while Mem_Flag1 == 1:										# si el flag es true read values

					#Lectura de valores en el PLC 
					Value1 = ReadDBlock(myplc,1501,46,3,S7WLBit)	#MODIFY
					TagID1 = 'Starter Compressor H2'				#MODIFY
					if Value1 == True:
						Value1 = 1
					if Value1 == False:
						Value1 = 0
					#print('1.- ' + str(Value1))

					Value2 = ReadDBlock(myplc,1501,46,4,S7WLBit)	#MODIFY
					TagID2 = 'Starter Compressor H2 defaut'			#MODIFY
					if Value2 == True:
						Value2 = 1
					if Value2 == False:
						Value2 = 0
					#print('2.- ' + str(Value2))

					Value3 = ReadDBlock(myplc,1601,40,0,S7WLReal)	#MODIFY
					TagID3 = 'L1 Amperes' 							#MODIFY
					if Value3 == True:
						Value3 = 1
					if Value3 == False:
						Value3 = 0
					#print('3.- ' + str(Value3))

					Value4 = ReadDBlock(myplc,1503,124,0,S7WLReal)	#MODIFY
					TagID4 = 'test1'							#MODIFY
					if Value4 == True:
						Value4 = 1
					if Value4 == False:
						Value4 = 0
					#print('4.- ' + str(Value4))

					Value5 = ReadDBlock(myplc,1503,96,0,S7WLReal)	#MODIFY
					TagID5 = 'test2'							#MODIFY
					if Value5 == True:
						Value5 = 1
					if Value5 == False:
						Value5 = 0
					#print('5.- ' + str(Value5))

					Value6 = ReadDBlock(myplc,1503,100,0,S7WLReal)		#MODIFY
					TagID6 = 'test3'								#MODIFY					
					if Value6 == True:
						Value6 = 1
					if Value6 == False:
						Value6 = 0
					#print('6.- ' + str(Value6))

					Value7 = ReadDBlock(myplc,1501,46,5,S7WLBit)		#MODIFY
					TagID7 = 'SPARE2'								#MODIFY
					if Value7 == True:
						Value7 = 1
					if Value7 == False:
						Value7 = 0
					#print('7.- ' + str(Value7))

					Value8 = ReadDBlock(myplc,1503,156,0,S7WLReal)		#MODIFY
					TagID8 = 'SANA'								#MODIFY
					if Value8 == True:
						Value8 = 1
					if Value8 == False:
						Value8 = 0
					#print('8.- ' + str(Value8))

					Value9 = ReadDBlock(myplc,1581,0,1,S7WLBit)		#MODIFY
					TagID9 = 'SPARE4'								#MODIFY
					if Value9 == True:
						Value9 = 1
					if Value9 == False:
						Value9 = 0
					#print('9.- ' + str(Value9))

					Value10 = ReadDBlock(myplc,1581,0,1,S7WLBit)	#MODIFY
					TagID10 = 'SPARE5'								#MODIFY
					if Value10 == True:
						Value10 = 1
					if Value10 == False:
						Value10 = 0
					#print('10.- ' + str(Value10))
					
					
					Time = datetime.now()	


					flagValue1 = 0
					flagValue2 = 0
					flagValue3 = 0
					flagValue4 = 0
					flagValue5 = 0
					flagValue6 = 0
					flagValue7 = 0
					flagValue8 = 0
					flagValue9 = 0
					flagValue10 = 0
					flagValueTime = 0





					# Append en la lista de memoria
				
					Y_Value1.append(Value1)
					flagValue1 = 1
					Y_Value2.append(Value2)
					flagValue2 = 1
					Y_Value3.append(Value3)
					flagValue3 = 1
					Y_Value4.append(Value4)
					flagValue4 = 1
					Y_Value5.append(Value5)
					flagValue5 = 1
					Y_Value6.append(Value6)
					flagValue6 = 1
					Y_Value7.append(Value7)
					flagValue7 = 1
					Y_Value8.append(Value8)
					flagValue8 = 1
					Y_Value9.append(Value9)
					flagValue9 = 1
					Y_Value10.append(Value10)
					flagValue10 = 1
					
					
					X_val.append(Time)
					flagValueTime = 1





					
					LOOPNumber = LOOPNumber + 1
					print('Data Logged:' + str(LOOPNumber))
					sleep(0.2)
					# Verificacion si la Distribucion Termino
					Start_Distribution_D1 = ReadDBlock(myplc,1581,0,2,S7WLBit)

					if Start_Distribution_D1 == 0 and Mem_Flag1 == 1:
						Mem_Flag3 = 1
						print("\n")
						print("Logging Deactivated...")
						Mem_Flag1 = 0
			





	window.after(800,loop)







#GUI Functions

def onChangeValue_Project(object):
	global Value0

	Value0 = combobox_Project.get()
	print(Value0)





#Register 1
def onChangeValue(object):
	global Value1

	Value1 = combobox2.get()
	print(Value1)
	AddressString2_Reg1['bg'] = 'red'
	AddressString2_Reg1['text'] = ''

def Combobox3_Change(object):
	global Value2

	Value2 = combobox3.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg1['bg'] = 'red'
	AddressString2_Reg1['text'] = ''
	


#Register 2
def onChangeValue_Reg2(object):
	global Value1_Reg2

	Value1_Reg2 = combobox2_Reg2.get()
	print(Value1_Reg2)
	AddressString2_Reg2['bg'] = 'red'
	AddressString2_Reg2['text'] = ''

def Combobox3_Change_Reg2(object):
	global Value2_Reg2

	Value2_Reg2 = combobox3_Reg2.get()
	print(Value2_Reg2) # Get Value selected from Combobox
	AddressString2_Reg2['bg'] = 'red'
	AddressString2_Reg2['text'] = ''


#Register 3
def onChangeValue_Reg3(object):
	global Value1

	Value1 = combobox2_Reg3.get()
	print(Value1)
	AddressString2_Reg3['bg'] = 'red'
	AddressString2_Reg3['text'] = ''

def Combobox3_Change_Reg3(object):
	global Value2

	Value2 = combobox3_Reg3.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg3['bg'] = 'red'
	AddressString2_Reg3['text'] = ''


#Register 4
def onChangeValue_Reg4(object):
	global Value1

	Value1 = combobox2_Reg4.get()
	print(Value1)
	AddressString2_Reg4['bg'] = 'red'
	AddressString2_Reg4['text'] = ''

def Combobox3_Change_Reg4(object):
	global Value2

	Value2 = combobox3_Reg4.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg4['bg'] = 'red'
	AddressString2_Reg4['text'] = ''


#Register 5
def onChangeValue_Reg5(object):
	global Value1

	Value1 = combobox2_Reg5.get()
	print(Value1)
	AddressString2_Reg5['bg'] = 'red'
	AddressString2_Reg5['text'] = ''

def Combobox3_Change_Reg5(object):
	global Value2

	Value2 = combobox3_Reg5.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg5['bg'] = 'red'
	AddressString2_Reg5['text'] = ''


#Register 6
def onChangeValue_Reg6(object):
	global Value1

	Value1 = combobox2_Reg6.get()
	print(Value1)
	AddressString2_Reg6['bg'] = 'red'
	AddressString2_Reg6['text'] = ''

def Combobox3_Change_Reg6(object):
	global Value2

	Value2 = combobox3_Reg6.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg6['bg'] = 'red'
	AddressString2_Reg6['text'] = ''


#Register 7
def onChangeValue_Reg7(object):
	global Value1

	Value1 = combobox2_Reg7.get()
	print(Value1)
	AddressString2_Reg7['bg'] = 'red'
	AddressString2_Reg7['text'] = ''

def Combobox3_Change_Reg7(object):
	global Value2

	Value2 = combobox3_Reg7.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg7['bg'] = 'red'
	AddressString2_Reg7['text'] = ''



#Register 8
def onChangeValue_Reg8(object):
	global Value1

	Value1 = combobox2_Reg8.get()
	print(Value1)
	AddressString2_Reg8['bg'] = 'red'
	AddressString2_Reg8['text'] = ''

def Combobox3_Change_Reg8(object):
	global Value2

	Value2 = combobox3_Reg8.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg8['bg'] = 'red'
	AddressString2_Reg8['text'] = ''



#Register 9
def onChangeValue_Reg9(object):
	global Value1

	Value1 = combobox2_Reg9.get()
	print(Value1)
	AddressString2_Reg9['bg'] = 'red'
	AddressString2_Reg9['text'] = ''

def Combobox3_Change_Reg9(object):
	global Value2

	Value2 = combobox3_Reg9.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg9['bg'] = 'red'
	AddressString2_Reg9['text'] = ''


#Register 10
def onChangeValue_Reg10(object):
	global Value1

	Value1 = combobox2_Reg10.get()
	print(Value1)
	AddressString2_Reg10['bg'] = 'red'
	AddressString2_Reg10['text'] = ''

def Combobox3_Change_Reg10(object):
	global Value2

	Value2 = combobox3_Reg10.get()
	print(Value2) # Get Value selected from Combobox
	AddressString2_Reg10['bg'] = 'red'
	AddressString2_Reg10['text'] = ''






def GetTextBoxfromBox():
	Text = TextBox1.get()	# Take Value from Text and we save it on Text variable
	l3['text'] = Text    	# update value from label GUI 
	print(Text) 			# Print Value Obtained.



def filterproject(DF_DataBase,Value0):
	global NameList
	global DF_DataBase2

	if Value0 == 'HRS-H2M':
		DF_DataBase2 = DF_DataBase[DF_DataBase['HRS-H2M'].str.contains('YES')]


#Register 1
def filterconcept(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3['values'] = NameList

def filterobject(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg1['text'] = Dataconcat1
		AddressString2_Reg1['bg'] = 'green'
		AddressString2_Reg1['text'] = 'Saved'


#Register 2
def filterconcept_Reg2(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg2['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg2['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg2['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg2['values'] = NameList

def filterobject_Reg2(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg2['text'] = Dataconcat1
		AddressString2_Reg2['bg'] = 'green'
		AddressString2_Reg2['text'] = 'Saved'


#Register 3
def filterconcept_Reg3(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg3['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg3['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg3['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg3['values'] = NameList

def filterobject_Reg3(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg3['text'] = Dataconcat1
		AddressString2_Reg3['bg'] = 'green'
		AddressString2_Reg3['text'] = 'Saved'




#Register 4
def filterconcept_Reg4(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg4['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg4['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg4['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg4['values'] = NameList

def filterobject_Reg4(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg4['text'] = Dataconcat1
		AddressString2_Reg4['bg'] = 'green'
		AddressString2_Reg4['text'] = 'Saved'



#Register 5
def filterconcept_Reg5(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg5['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg5['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg5['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg5['values'] = NameList

def filterobject_Reg5(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg5['text'] = Dataconcat1
		AddressString2_Reg5['bg'] = 'green'
		AddressString2_Reg5['text'] = 'Saved'



#Register 6
def filterconcept_Reg6(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg6['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg6['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg6['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg6['values'] = NameList

def filterobject_Reg6(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg6['text'] = Dataconcat1
		AddressString2_Reg6['bg'] = 'green'
		AddressString2_Reg6['text'] = 'Saved'



#Register 7
def filterconcept_Reg7(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg7['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg7['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg7['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg7['values'] = NameList

def filterobject_Reg7(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg7['text'] = Dataconcat1
		AddressString2_Reg7['bg'] = 'green'
		AddressString2_Reg7['text'] = 'Saved'



#Register 8
def filterconcept_Reg8(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg8['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg8['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg8['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg8['values'] = NameList

def filterobject_Reg8(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg8['text'] = Dataconcat1
		AddressString2_Reg8['bg'] = 'green'
		AddressString2_Reg8['text'] = 'Saved'



#Register 9
def filterconcept_Reg9(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg9['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg9['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg9['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg9['values'] = NameList

def filterobject_Reg9(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg9['text'] = Dataconcat1
		AddressString2_Reg9['bg'] = 'green'
		AddressString2_Reg9['text'] = 'Saved'


#Register 10
def filterconcept_Reg10(DF_DataBase2,Value1):
	global NameList
	global DatabaseFiltrado

	if Value1 == 'Measure':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Measure')]
		NameList = DatabaseFiltrado['PID TAG'].tolist()
		combobox3_Reg10['values'] = NameList
	elif Value1 == 'Status':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Status')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg10['values'] = NameList
	elif Value1 == 'Defaut':
		DatabaseFiltrado = DF_DataBase2[DF_DataBase2['Concept'].str.contains('Defaut')]
		NameList = DatabaseFiltrado['NAME'].tolist()
		combobox3_Reg10['values'] = NameList
	else: 
		NameList = ['< select Concept >']
		combobox3_Reg10['values'] = NameList

def filterobject_Reg10(DF_DataBasefiltrado,Value2):
	global DatabaseFiltrado

	addressDF = DF_DataBasefiltrado[DF_DataBasefiltrado.isin([Value2]).any(axis=1)]
	addressDF[custom_sort]
	print(addressDF)
	RowNumbers = addressDF['No'].count()
	
	if RowNumbers == 1:
		Var_DB = addressDF.iloc[0,2]
		print('DB: ' + str(Var_DB))

		Var_Byte = addressDF.iloc[0,3]
		Var_Byte_INT = int(Var_Byte)
		print('DB: ' + str(Var_Byte_INT))

		Var_Bit = addressDF.iloc[0,4]
		print('DB: ' + str(Var_Bit))

		Var_DataType = addressDF.iloc[0,5]
		print('DB: ' + str(Var_DataType))

		Dataconcat1 = 'DB' + str(Var_DB) + ' ' + str(Var_DataType) + ' ' + str(Var_Byte_INT) + '.' + str(Var_Bit)
		AddressString_Reg10['text'] = Dataconcat1
		AddressString2_Reg10['bg'] = 'green'
		AddressString2_Reg10['text'] = 'Saved'




#Data Management Functions
def InitDataFrames(StartupFile):
	df_Init = pd.read_excel(StartupFile)
	return df_Init
	#df_Init.to_excel(path, index=False)




# INIT
DB = 1586
custom_sort = ['No', 'NAME', 'DB', 'Address Byte', 'Address Bit', 'DataType', 'Concept', 'PID TAG', 'HRS-H2M', 'Log']

DF_DataBase=InitDataFrames(KeyFile)
DF_DataBase= DF_DataBase.replace(r'^\s+$', np.nan, regex=True)
print(DF_DataBase)
#DatabaseFiltrado = DF_DataBase[DF_DataBase['Log'] == 1]




#Widgets --------------------------------------------------------------------------------------------------------------------------------

#Labels

lProject = Label(window,text='Project: ')
lProject.grid(row = 0, column = 0)



#Register 1
label_Reg1 = Label(window,text='REGISTER #1')
label_Reg1.grid(row = 3, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 4, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 5, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 6, column = 0)


#Register 2
label_Reg2 = Label(window,text='REGISTER #2')
label_Reg2.grid(row = 8, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 9, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 10, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 11, column = 0)



#Register 3
label_Reg3 = Label(window,text='REGISTER #3')
label_Reg3.grid(row = 13, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 14, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 15, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 16, column = 0)



#Register 4
label_Reg4 = Label(window,text='REGISTER #4')
label_Reg4.grid(row = 18, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 19, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 20, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 21, column = 0)


#Register 5
label_Reg5 = Label(window,text='REGISTER #5')
label_Reg5.grid(row = 23, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 24, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 25, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 26, column = 0)


#Register 6
label_Reg6 = Label(window,text='REGISTER #6')
label_Reg6.grid(row = 28, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 29, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 30, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 31, column = 0)


#Register 7
label_Reg7 = Label(window,text='REGISTER #7')
label_Reg7.grid(row = 33, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 34, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 35, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 36, column = 0)



#Register 8
label_Reg8 = Label(window,text='REGISTER #8')
label_Reg8.grid(row = 38, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 39, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 40, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 41, column = 0)



#Register 9
label_Reg9 = Label(window,text='REGISTER #9')
label_Reg9.grid(row = 43, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 44, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 45, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 46, column = 0)


#Register 10
label_Reg10 = Label(window,text='REGISTER #10')
label_Reg10.grid(row = 48, column = 1)


l30 = Label(window,text='Concept: ')
l30.grid(row = 49, column = 0)

l40 = Label(window,text='Object: ')
l40.grid(row = 50, column = 0)

l50 = Label(window,text='Address: ')
l50.grid(row = 51, column = 0)







#Reg1
AddressString_Reg1 = Label(window,text='String Address')
AddressString_Reg1.grid(row = 6, column = 1)

AddressString2_Reg1 = Label(window, width= 10, height=1)
AddressString2_Reg1.grid(row = 6, column = 2)
AddressString2_Reg1['bg'] = 'red'

#Reg2
AddressString_Reg2 = Label(window,text='String Address')
AddressString_Reg2.grid(row = 11, column = 1)

AddressString2_Reg2 = Label(window, width= 10, height=1)
AddressString2_Reg2.grid(row = 11, column = 2)
AddressString2_Reg2['bg'] = 'red'

#Reg3
AddressString_Reg3 = Label(window,text='String Address')
AddressString_Reg3.grid(row = 16, column = 1)

AddressString2_Reg3 = Label(window, width= 10, height=1)
AddressString2_Reg3.grid(row = 16, column = 2)
AddressString2_Reg3['bg'] = 'red'

#Reg4
AddressString_Reg4 = Label(window,text='String Address')
AddressString_Reg4.grid(row = 21, column = 1)

AddressString2_Reg4 = Label(window, width= 10, height=1)
AddressString2_Reg4.grid(row = 21, column = 2)
AddressString2_Reg4['bg'] = 'red'

#Reg5
AddressString_Reg5 = Label(window,text='String Address')
AddressString_Reg5.grid(row = 26, column = 1)

AddressString2_Reg5 = Label(window, width= 10, height=1)
AddressString2_Reg5.grid(row = 26, column = 2)
AddressString2_Reg5['bg'] = 'red'

#Reg6
AddressString_Reg6 = Label(window,text='String Address')
AddressString_Reg6.grid(row = 31, column = 1)

AddressString2_Reg6 = Label(window, width= 10, height=1)
AddressString2_Reg6.grid(row = 31, column = 2)
AddressString2_Reg6['bg'] = 'red'

#Reg7
AddressString_Reg7 = Label(window,text='String Address')
AddressString_Reg7.grid(row = 36, column = 1)

AddressString2_Reg7 = Label(window, width= 10, height=1)
AddressString2_Reg7.grid(row = 36, column = 2)
AddressString2_Reg7['bg'] = 'red'

#Reg8
AddressString_Reg8 = Label(window,text='String Address')
AddressString_Reg8.grid(row = 41, column = 1)

AddressString2_Reg8 = Label(window, width= 10, height=1)
AddressString2_Reg8.grid(row = 41, column = 2)
AddressString2_Reg8['bg'] = 'red'

#Reg9
AddressString_Reg9 = Label(window,text='String Address')
AddressString_Reg9.grid(row = 46, column = 1)

AddressString2_Reg9 = Label(window, width= 10, height=1)
AddressString2_Reg9.grid(row = 46, column = 2)
AddressString2_Reg9['bg'] = 'red'

#Reg10
AddressString_Reg10 = Label(window,text='String Address')
AddressString_Reg10.grid(row = 51, column = 1)

AddressString2_Reg10 = Label(window, width= 10, height=1)
AddressString2_Reg10.grid(row = 51, column = 2)
AddressString2_Reg10['bg'] = 'red'





#ComboBox
combobox_Project = Combobox(window,values=['HRS-CNR', 'HRS-APEX', 'HRS-H2M'])
combobox_Project.grid(row = 0, column = 1)
combobox_Project.bind('<<ComboboxSelected>>',onChangeValue_Project)



# Register 1
combobox2 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2.grid(row = 4, column = 1)
combobox2.bind('<<ComboboxSelected>>',onChangeValue)

combobox3 = Combobox(window,values=NameList)
combobox3.grid(row = 5, column = 1)
combobox3.bind('<<ComboboxSelected>>',Combobox3_Change)


# Register 2
combobox2_Reg2 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg2.grid(row = 9, column = 1)
combobox2_Reg2.bind('<<ComboboxSelected>>',onChangeValue_Reg2)

combobox3_Reg2 = Combobox(window,values=NameList)
combobox3_Reg2.grid(row = 10, column = 1)
combobox3_Reg2.bind('<<ComboboxSelected>>',Combobox3_Change_Reg2)



# Register 3
combobox2_Reg3 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg3.grid(row = 14, column = 1)
combobox2_Reg3.bind('<<ComboboxSelected>>',onChangeValue_Reg3)

combobox3_Reg3 = Combobox(window,values=NameList)
combobox3_Reg3.grid(row = 15, column = 1)
combobox3_Reg3.bind('<<ComboboxSelected>>',Combobox3_Change_Reg3)


# Register 4
combobox2_Reg4 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg4.grid(row = 19, column = 1)
combobox2_Reg4.bind('<<ComboboxSelected>>',onChangeValue_Reg4)

combobox3_Reg4 = Combobox(window,values=NameList)
combobox3_Reg4.grid(row = 20, column = 1)
combobox3_Reg4.bind('<<ComboboxSelected>>',Combobox3_Change_Reg4)



# Register 5
combobox2_Reg5 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg5.grid(row = 24, column = 1)
combobox2_Reg5.bind('<<ComboboxSelected>>',onChangeValue_Reg5)

combobox3_Reg5 = Combobox(window,values=NameList)
combobox3_Reg5.grid(row = 25, column = 1)
combobox3_Reg5.bind('<<ComboboxSelected>>',Combobox3_Change_Reg5)


# Register 6
combobox2_Reg6 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg6.grid(row = 29, column = 1)
combobox2_Reg6.bind('<<ComboboxSelected>>',onChangeValue_Reg6)

combobox3_Reg6 = Combobox(window,values=NameList)
combobox3_Reg6.grid(row = 30, column = 1)
combobox3_Reg6.bind('<<ComboboxSelected>>',Combobox3_Change_Reg6)


# Register 7
combobox2_Reg7 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg7.grid(row = 34, column = 1)
combobox2_Reg7.bind('<<ComboboxSelected>>',onChangeValue_Reg7)

combobox3_Reg7 = Combobox(window,values=NameList)
combobox3_Reg7.grid(row = 35, column = 1)
combobox3_Reg7.bind('<<ComboboxSelected>>',Combobox3_Change_Reg7)



# Register 8
combobox2_Reg8 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg8.grid(row = 39, column = 1)
combobox2_Reg8.bind('<<ComboboxSelected>>',onChangeValue_Reg8)

combobox3_Reg8 = Combobox(window,values=NameList)
combobox3_Reg8.grid(row = 40, column = 1)
combobox3_Reg8.bind('<<ComboboxSelected>>',Combobox3_Change_Reg8)


# Register 9
combobox2_Reg9 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg9.grid(row = 44, column = 1)
combobox2_Reg9.bind('<<ComboboxSelected>>',onChangeValue_Reg9)

combobox3_Reg9 = Combobox(window,values=NameList)
combobox3_Reg9.grid(row = 45, column = 1)
combobox3_Reg9.bind('<<ComboboxSelected>>',Combobox3_Change_Reg9)



# Register 10
combobox2_Reg10 = Combobox(window,values=['Measure', 'Status', 'Defaut'])
combobox2_Reg10.grid(row = 49, column = 1)
combobox2_Reg10.bind('<<ComboboxSelected>>',onChangeValue_Reg10)

combobox3_Reg10 = Combobox(window,values=NameList)
combobox3_Reg10.grid(row = 50, column = 1)
combobox3_Reg10.bind('<<ComboboxSelected>>',Combobox3_Change_Reg10)








#Buttons
button_get_value = Button(window,text='Connect to PLC BPCS/PSD', command=StartProgram)
#button_get_value.pack(side=LEFT)
button_get_value.grid(row = 0, column = 8)

button_get_valuedis = Button(window,text='Disconnect to PLC BPCS/PSD', command=CloseProgram)
#button_get_value.pack(side=LEFT)
button_get_valuedis.grid(row = 1, column = 8)


button_filterconcept_Project = Button(window,text='Confirm Project', command= lambda: filterproject(DF_DataBase,Value0))
button_filterconcept_Project.grid(row = 0, column = 2)



#Register 1
button_filterconcept_Reg1 = Button(window,text='Confirm Concept', command= lambda: filterconcept(DF_DataBase2,Value1))
button_filterconcept_Reg1.grid(row = 4, column = 2)

button_filterconcept_Reg1 = Button(window,text='Confirm Object', command= lambda: filterobject(DatabaseFiltrado,Value2))
button_filterconcept_Reg1.grid(row = 5, column = 2)


#Register 2
button_filterconcept_Reg2 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg2(DF_DataBase2,Value1_Reg2))
button_filterconcept_Reg2.grid(row = 9, column = 2)

button_filterconcept_Reg2 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg2(DatabaseFiltrado,Value2_Reg2))
button_filterconcept_Reg2.grid(row = 10, column = 2)


#Register 3
button_filterconcept_Reg3 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg3(DF_DataBase2,Value1))
button_filterconcept_Reg3.grid(row = 14, column = 2)

button_filterconcept_Reg3 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg3(DatabaseFiltrado,Value2))
button_filterconcept_Reg3.grid(row = 15, column = 2)


#Register 4
button_filterconcept_Reg4 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg4(DF_DataBase2,Value1))
button_filterconcept_Reg4.grid(row = 19, column = 2)

button_filterconcept_Reg4 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg4(DatabaseFiltrado,Value2))
button_filterconcept_Reg4.grid(row = 20, column = 2)


#Register 5
button_filterconcept_Reg5 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg5(DF_DataBase2,Value1))
button_filterconcept_Reg5.grid(row = 24, column = 2)

button_filterconcept_Reg5 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg5(DatabaseFiltrado,Value2))
button_filterconcept_Reg5.grid(row = 25, column = 2)


#Register 6
button_filterconcept_Reg6 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg6(DF_DataBase2,Value1))
button_filterconcept_Reg6.grid(row = 29, column = 2)

button_filterconcept_Reg6 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg6(DatabaseFiltrado,Value2))
button_filterconcept_Reg6.grid(row = 30, column = 2)


#Register 7
button_filterconcept_Reg7 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg7(DF_DataBase2,Value1))
button_filterconcept_Reg7.grid(row = 34, column = 2)

button_filterconcept_Reg7 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg7(DatabaseFiltrado,Value2))
button_filterconcept_Reg7.grid(row = 35, column = 2)


#Register 8
button_filterconcept_Reg8 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg8(DF_DataBase2,Value1))
button_filterconcept_Reg8.grid(row = 39, column = 2)

button_filterconcept_Reg8 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg8(DatabaseFiltrado,Value2))
button_filterconcept_Reg8.grid(row = 40, column = 2)


#Register 9
button_filterconcept_Reg9 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg9(DF_DataBase2,Value1))
button_filterconcept_Reg9.grid(row = 44, column = 2)

button_filterconcept_Reg9 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg9(DatabaseFiltrado,Value2))
button_filterconcept_Reg9.grid(row = 45, column = 2)


#Register 10
button_filterconcept_Reg10 = Button(window,text='Confirm Concept', command= lambda: filterconcept_Reg10(DF_DataBase2,Value1))
button_filterconcept_Reg10.grid(row = 49, column = 2)

button_filterconcept_Reg10 = Button(window,text='Confirm Object', command= lambda: filterobject_Reg10(DatabaseFiltrado,Value2))
button_filterconcept_Reg10.grid(row = 50, column = 2)





#TextBox
TextBox1 = Entry(window)
#TextBox1.pack()
#TextBox1.grid(row = 5, column = 2)




#Listbox
testdicc = {0:'Raul',1:'juan'}
listbox = Listbox(window)
listbox.insert(0,'Raul')
listbox.insert(1,'Pedro')

#listbox.pack(side=RIGHT)
#listbox.grid(row = 6, column = 6)









window.after(800,loop)

window.mainloop()




#Extras

# Seperator object 
#separator = ttk.Separator(window, orient='horizontal') 
#separator.place(relx=0, rely=0.03, relwidth=1, relheight=1) 