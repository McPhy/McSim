#McSIM 

#----------------------------------------- Import Modules and packages ----------------------------------------------

# Time package
from time import sleep 

# Snap 7 package
import snap7
from time import sleep 
import snap7.client as c 
from snap7.util import *
from snap7.snap7types import *
from datetime import datetime

# Anaconda Packages
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np 
import pandas as pd
from pandas.plotting import register_matplotlib_converters

# OS
import os

 
#----------------------------------------- Funciones de lectura y escritura ---------------------------------------
#------------------------------------------------------------------------------------------------------------------

#Lectura en Memoria del PLC "M"
def ReadMemory(plc,byte,bit,datatype):
	result = plc.read_area(areas['MK'],0,byte,datatype)
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

#Escritura en Memoria del PLC "M"
def WriteMemory(plc,byte,bit,datatype,value):
	result = plc.read_area(areas['MK'],0,byte,datatype)
	if datatype == S7WLBit:
		set_bool(result,0,bit,value)
	elif datatype == S7WLByte or datatype == S7WLWord:
		set_int(result,0,value)
	elif datatype == S7WLReal:
		set_real(result,0,value)
	elif datatype == S7WLDWord:
		set_dword(result,0,value)
	plc.write_area(areas['MK'],0,byte,result)
		

#Lecrura en Entrada del PLC "I"
def ReadInput(plc,byte,bit,datatype):
	result = plc.read_area(areas['PE'],0,byte,datatype)
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

#Escritura en Entrada del PLC "I"
def WriteInput(plc,byte,bit,datatype,value):
	result = plc.read_area(areas['PE'],0,byte,datatype)
	if datatype == S7WLBit:
		set_bool(result,0,bit,value)
	elif datatype == S7WLByte or datatype == S7WLWord:
		set_int(result,0,value)
	elif datatype == S7WLReal:
		set_real(result,0,value)
	elif datatype == S7WLDWord:
		set_dword(result,0,value)
	plc.write_area(areas['PE'],0,byte,result)

#Lectura de Salidas del PLC "Q"
def ReadOutput(plc,byte,bit,datatype):
	result = plc.read_area(areas['PA'],0,byte,datatype)
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

#Lectura de Salida del PLC "Q"
def WriteOutput(plc,byte,bit,datatype,value):
	result = plc.read_area(areas['PA'],0,byte,datatype)
	if datatype == S7WLBit:
		set_bool(result,0,bit,value)
	elif datatype == S7WLByte or datatype == S7WLWord:
		set_int(result,0,value)
	elif datatype == S7WLReal:
		set_real(result,0,value)
	elif datatype == S7WLDWord:
		set_dword(result,0,value)
	plc.write_area(areas['PA'],0,byte,result)


#Lectura de DB del PLC "DB"
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

#Escritura de DB del PLC "DB"
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



#--------------------------------------------- [ Snap 7 - Client Connection ] -------------------------------------------
#Estableciendo Cliente y Conexion el Automata

myplc = snap7.client.Client()
myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 


#Call Funcion para conectarse al servidor como cliente
ETAT = myplc.get_connected()
print('Conection Established: ' + str(ETAT))


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




while True:

	try:

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
					sleep(5)
					# Verificacion si la Distribucion Termino
					Start_Distribution_D1 = ReadDBlock(myplc,1581,0,2,S7WLBit)

					if Start_Distribution_D1 == 0 and Mem_Flag1 == 1:
						Mem_Flag3 = 1
						print("\n")
						print("Logging Deactivated...")
						Mem_Flag1 = 0
			

			'''
			######## Subrutina de para crear el Data Frame
			if Mem_Flag3 == 1:
				print("\n")
				print("Creating Excel DataFrame...")
				df = pd.DataFrame()				# Creacion del Data frame para concaternar los valores de los sensores
				df[TagName1] = Y_Value1
				df[TagName2] = Y_Value2
				df[TagName3] = Y_Value3
				df[TagName4] = Y_Value4
				df[TagName5] = Y_Value5
				df[TagName6] = Y_Value6
				df[TagName7] = Y_Value7
				df[TagName8] = Y_Value8
				df[TagName9] = Y_Value9
				df[TagName10] = Y_Value10


				dfxls = pd.DataFrame()				# Creacion del Data frame para concaternar los valores de los sensores
				dfxls[TagID1] = Y_Value1
				dfxls[TagID2] = Y_Value2
				dfxls[TagID3] = Y_Value3
				dfxls[TagID4] = Y_Value4
				dfxls[TagID5] = Y_Value5
				dfxls[TagID6] = Y_Value6
				dfxls[TagID7] = Y_Value7
				dfxls[TagID8] = Y_Value8
				dfxls[TagID9] = Y_Value9
				dfxls[TagID10] = Y_Value10
				

				df['Time'] = X_val
				dfxls['Time'] = X_val

				custom_sort = ['Time', TagID1, TagID2, TagID3, TagID4, TagID5, TagID6, TagID7, TagID8, TagID9, TagID10]
				FilterDF = dfxls[custom_sort]

				timeReg = datetime.now()
				dt_string = timeReg.strftime("%d/%m/%Y %H:%M:%S")
				path = LogFolder + 'LogFile_' + dt_string[0] + dt_string[1] + dt_string[3] + dt_string[4] + '_' +dt_string[11] + dt_string[12] + dt_string[14] + dt_string[15] + '_' + dt_string[17] + dt_string[18] + '.xlsx'

				FilterDF.to_excel(path, index=False)


				Decision = input('Create a Graph? [Yes/No]')

				if Decision == 'yes' or Decision == 'Yes' or Decision == 'YES' or Decision == 'y':
					
					plt.figure(figsize=(14,8))
					TittleGraph = 'McView Data Logged'
					plt.title(TittleGraph, fontdict={'fontweight':'bold','fontsize':18})

					#Colors (b,g,r,c,m,y,k,w)

					plt.plot(df.Time, df.value1, 'b', ms= 9, label=TagID1)
					plt.plot(df.Time, df.value2, 'g', ms= 9, label=TagID2)
					plt.plot(df.Time, df.value3, 'r', ms= 9, label=TagID3)
					plt.plot(df.Time, df.value4, 'c', ms= 9, label=TagID4)
					plt.plot(df.Time, df.value5, 'm', ms= 9, label=TagID5)
					plt.plot(df.Time, df.value6, 'y.', ms= 9, label=TagID6)
					plt.plot(df.Time, df.value7, 'k.', ms= 9, label=TagID7)
					plt.plot(df.Time, df.value8, 'w.', ms= 9, label=TagID8)
					plt.plot(df.Time, df.value9, 'w.', ms= 9, label=TagID9)
					plt.plot(df.Time, df.value10, 'w.', ms= 9, label=TagID10)


					#plt.xticks(c.x_axis)
					plt.xticks(rotation=45)
					plt.xticks(fontsize=12) 
					plt.legend()
					ax = plt.gca()
					xfmt = md.DateFormatter('%H:%M:%S')
					ax.xaxis.set_major_formatter(xfmt)
					plt.xlabel('Time')
					plt.ylabel('Values')
					plt.tight_layout()

					#plt.savefig('Graphp1',dpi=300)
					plt.show()
					plt.clf()

					Mem_Flag3 = 0
					print("\n")
					print('The operation was carried out successfully.')
					sleep(3)
					print("\n")
					print('You can Start a new File Logging....')
					print("\n")


				else:
					Mem_Flag3 = 0
					print("\n")
					print('The operation was carried out successfully.')
					sleep(3)
					print("\n")
					print('You can Start a new File Logging....')
					print("\n")
				'''

	except:
		ETAT = 0
		#LOOPNumber = 0
		if flagValue1 == 0:
			Y_Value1.append(Value1)
			flagValue1 = 1
		if flagValue2 == 0:
			Y_Value2.append(Value2)
			flagValue2 = 1
		if flagValue3 == 0:
			Y_Value3.append(Value3)
			flagValue3 = 1
		if flagValue4 == 0:
			Y_Value4.append(Value4)
			flagValue4 = 1
		if flagValue5 == 0:
			Y_Value5.append(Value5)
			flagValue5 = 1
		if flagValue6 == 0:
			Y_Value6.append(Value6)
			flagValue6 = 1
		if flagValue7 == 0:
			Y_Value7.append(Value7)
			flagValue7 = 1
		if flagValue8 == 0:
			Y_Value8.append(Value8)
			flagValue8 = 1
		if flagValue9 == 0:
			Y_Value9.append(Value9)
			flagValue9 = 1
		if flagValue10 == 0:
			Y_Value10.append(Value10)
			flagValue10 = 1
		if flagValueTime == 0:
			X_val.append(Time)
			flagValueTime = 1	

		print('E-catcher Connection Problem')
		print('Trying to reconnect...')
		pass



######## Subrutina de para crear el Data Frame
	if Mem_Flag3 == 1:
		print("\n")
		print("Creating Excel DataFrame...")
		df = pd.DataFrame()				# Creacion del Data frame para concaternar los valores de los sensores
		df[TagName1] = Y_Value1
		df[TagName2] = Y_Value2
		df[TagName3] = Y_Value3
		df[TagName4] = Y_Value4
		df[TagName5] = Y_Value5
		df[TagName6] = Y_Value6
		df[TagName7] = Y_Value7
		df[TagName8] = Y_Value8
		df[TagName9] = Y_Value9
		df[TagName10] = Y_Value10


		dfxls = pd.DataFrame()				# Creacion del Data frame para concaternar los valores de los sensores
		dfxls[TagID1] = Y_Value1
		dfxls[TagID2] = Y_Value2
		dfxls[TagID3] = Y_Value3
		dfxls[TagID4] = Y_Value4
		dfxls[TagID5] = Y_Value5
		dfxls[TagID6] = Y_Value6
		dfxls[TagID7] = Y_Value7
		dfxls[TagID8] = Y_Value8
		dfxls[TagID9] = Y_Value9
		dfxls[TagID10] = Y_Value10
		

		df['Time'] = X_val
		dfxls['Time'] = X_val

		custom_sort = ['Time', TagID1, TagID2, TagID3, TagID4, TagID5, TagID6, TagID7, TagID8, TagID9, TagID10]
		FilterDF = dfxls[custom_sort]

		timeReg = datetime.now()
		dt_string = timeReg.strftime("%d/%m/%Y %H:%M:%S")
		path = LogFolder + 'LogFile_' + dt_string[0] + dt_string[1] + dt_string[3] + dt_string[4] + '_' +dt_string[11] + dt_string[12] + dt_string[14] + dt_string[15] + '_' + dt_string[17] + dt_string[18] + '.xlsx'

		FilterDF.to_excel(path, index=False)


		Decision = input('Create a Graph? [Yes/No]')

		if Decision == 'yes' or Decision == 'Yes' or Decision == 'YES' or Decision == 'y':
			
			plt.figure(figsize=(14,8))
			TittleGraph = 'McView Data Logged'
			plt.title(TittleGraph, fontdict={'fontweight':'bold','fontsize':18})

			#Colors (b,g,r,c,m,y,k,w)

			plt.plot(df.Time, df.value1, 'b', ms= 9, label=TagID1)
			plt.plot(df.Time, df.value2, 'g', ms= 9, label=TagID2)
			plt.plot(df.Time, df.value3, 'r', ms= 9, label=TagID3)
			plt.plot(df.Time, df.value4, 'c', ms= 9, label=TagID4)
			plt.plot(df.Time, df.value5, 'm', ms= 9, label=TagID5)
			plt.plot(df.Time, df.value6, 'y.', ms= 9, label=TagID6)
			plt.plot(df.Time, df.value7, 'k.', ms= 9, label=TagID7)
			plt.plot(df.Time, df.value8, 'w.', ms= 9, label=TagID8)
			plt.plot(df.Time, df.value9, 'w.', ms= 9, label=TagID9)
			plt.plot(df.Time, df.value10, 'w.', ms= 9, label=TagID10)


			#plt.xticks(c.x_axis)
			plt.xticks(rotation=45)
			plt.xticks(fontsize=12) 
			plt.legend()
			ax = plt.gca()
			xfmt = md.DateFormatter('%H:%M:%S')
			ax.xaxis.set_major_formatter(xfmt)
			plt.xlabel('Time')
			plt.ylabel('Values')
			plt.tight_layout()

			#plt.savefig('Graphp1',dpi=300)
			plt.show()
			plt.clf()

			Mem_Flag3 = 0
			print("\n")
			print('The operation was carried out successfully.')
			sleep(3)
			print("\n")
			print('You can Start a new File Logging....')
			print("\n")


		else:
			Mem_Flag3 = 0
			LOOPNumber = 0
			print("\n")
			print('The operation was carried out successfully.')
			sleep(3)
			print("\n")
			print('You can Start a new File Logging....')
			print("\n")






#===================================================================================================================