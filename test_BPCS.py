import pandas as pd
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
import tkinter as tk
from tkinter import filedialog



b = 0
tmp = 1
step  = 40
CMD = 0
CMD_V = False
adressByte = []
adressBit = []
dataType = []
dataName = []

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


myplc = snap7.client.Client()
myplc.connect('192.168.0.100',0,2) #adress, rack et slot in server 

print(myplc.get_connected())

APIstatus = myplc.get_cpu_state()
print("The Status of PLC is: " + APIstatus)
print("\n")

#Excel_file_name = input("Please enter the Excel file name:\n")

root  = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

df = pd.read_excel(file_path, sheet_name ='Sheet1', header=0)
#df = pd.read_excel(Excel_file_name, sheet_name ='Sheet1', header=0)
#b = 0
for i in range(len(df['NAME'])):
	if df['NAME'][i].find("Mode", 0, 4) != -1 :
		WriteDBlock(myplc,1586,int(df['Address Byte'][i]), int(df['Address Bit'][i]), S7WLBit, 1)
		#print(b, i, df['NAME'][i], int(df['Address Byte'][i]), df['Address Bit'][i])

for i in range(len(df['NAME'])):
	if df['NAME'][i].find("CMD", 0, 3) != -1 :
		adressByte.append(df['Address Byte'][i])
		adressBit.append(df['Address Bit'][i])
		dataType.append(df['DataType'][i])
		dataName.append(df['NAME'][i])
		# print(i, b, dataName[b], adressByte[b], adressBit[b], dataType[b])
		# b = b + 1

try :
	while True :
		if CMD <= 400 and tmp == 1:
			for x in range(0,10) :
				CMD = CMD + step
				if CMD_V == False : CMD_V = True
				elif CMD_V == True : CMD_V = False
				for i in range(len(adressByte)):
					if dataType[i] == "REAL" :
						WriteDBlock(myplc,1586,int(adressByte[i]), int(adressBit[i]), S7WLReal, CMD)
					elif dataType[i] == "BOOL":
						WriteDBlock(myplc,1586,int(adressByte[i]), int(adressBit[i]), S7WLBit, CMD_V)					
						#print(b, i, df['NAME'][i], int(df['Address Byte'][i]), df['Address Bit'][i])
				if CMD == 400 : tmp = 0

		if CMD >= 0 and tmp == 0 :
			for x in range(0,10) :
				CMD = CMD - step
				if CMD_V == False : CMD_V = True
				elif CMD_V == True : CMD_V = False
				for i in range(len(adressByte)):
					if dataType[i] == "REAL" :
						WriteDBlock(myplc,1586,int(adressByte[i]), int(adressBit[i]), S7WLReal, CMD)
					elif dataType[i] == "BOOL":
						WriteDBlock(myplc,1586,int(adressByte[i]), int(adressBit[i]), S7WLBit, CMD_V)
						#print(b, i, df['NAME'][i], int(df['Address Byte'][i]), df['Address Bit'][i])
				if CMD == 0 : tmp = 1

except KeyboardInterrupt:
	for i in range(len(df['NAME'])):
		if df['NAME'][i].find("Mode", 0, 4) != -1 :
			WriteDBlock(myplc,1586,int(df['Address Byte'][i]), int(df['Address Bit'][i]), S7WLBit, 0)

	for i in range(len(adressByte)):
		WriteDBlock(myplc,1586,int(adressByte[i]), int(adressBit[i]), S7WLReal, 0)