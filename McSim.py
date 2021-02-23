#McSIM 
import snap7
from time import sleep 
import snap7.client as c 
from snap7.util import *
from snap7.snap7types import *
 
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

#------------------------------------------------------------------------------------------------------------------
#Estableciendo Cliente y Conexion el Automata

myplc = snap7.client.Client()
myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 


#Call Funcion para ver si existe conectividad entre servidor y cliente
print(myplc.get_connected())


#Call funcion para ver estatus del PLC
APIstatus = myplc.get_cpu_state()
print("The Status of PLC is: " + APIstatus)
print("\n")

#COMMANDS
WriteDBlock(myplc,1586,694,0,S7WLBit,1)		#PT STK 1
WriteDBlock(myplc,1586,726,0,S7WLBit,1)		#PT STK 2
WriteDBlock(myplc,1586,758,0,S7WLBit,1)		#PT STK 3

#------------------------------ Algoritmo prueba de montar y demontar Presion ------------------------------------------------

aumento = 0
for x in range(0,20):

	aumento = aumento + 40.0 


	WriteDBlock(myplc,1586,696,0,S7WLReal,aumento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,682,0,S7WLReal)
	print(valorIN)

	WriteDBlock(myplc,1586,728,0,S7WLReal,aumento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,714,0,S7WLReal)
	print(valorIN)

	WriteDBlock(myplc,1586,760,0,S7WLReal,aumento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,746,0,S7WLReal)
	print(valorIN)





decremento = 800.0
for x in range(0,20):

	decremento = decremento - 40.0 

	WriteDBlock(myplc,1586,696,0,S7WLReal,decremento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,682,0,S7WLReal)
	print(valorIN)

	WriteDBlock(myplc,1586,728,0,S7WLReal,decremento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,714,0,S7WLReal)
	print(valorIN)

	WriteDBlock(myplc,1586,760,0,S7WLReal,decremento)
	sleep(0.2)
	valorIN = ReadDBlock(myplc,1586,746,0,S7WLReal)
	print(valorIN)




WriteDBlock(myplc,1586,694,0,S7WLBit,0)		#PT STK 1
WriteDBlock(myplc,1586,726,0,S7WLBit,0)		#PT STK 2
WriteDBlock(myplc,1586,758,0,S7WLBit,0)		#PT STK 3


#------------------------------------------------------------------------------------------------------------------





#---------------------------------------- Test de Funciones de Lectura y Escritura  ------------------------------------
'''
#Test Digital Input I0.0
WriteInput(myplc,0,0,S7WLBit,1)
valorIN = ReadInput(myplc,0,0,S7WLBit)
print(valorIN)


#Test Digital Input I0.1
WriteInput(myplc,0,1,S7WLBit,1)
valorIN = ReadInput(myplc,0,1,S7WLBit)
print(valorIN)


#Test analog Input IW554
WriteInput(myplc,554,0,S7WLWord,0.0)
valorIN = ReadInput(myplc,554,0,S7WLWord)
print(valorIN)



#Test Digital Output Q0.1
WriteOutput(myplc,0,1,S7WLBit,1)
valorIN = ReadOutput(myplc,0,1,S7WLBit)
print(valorIN)


#Test DB1502 byte 198 PT 3.1 tiene que estar en modo Forcage.
WriteDBlock(myplc,1502,198,0,S7WLReal,27.0)
valorIN = ReadDBlock(myplc,1502,198,0,S7WLReal)
print(valorIN)

'''


#------------------------------------------------------------------------------------------------------------------