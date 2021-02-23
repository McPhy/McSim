import pprint
import pandas as pd 
import numpy as np
from datetime import datetime
from time import sleep



KeyFile =  'C:\\Users\\admin\\Desktop\\McSIM\\DataLogSetup.xlsx'



def InitDataFrames(StartupFile):
	df_Init = pd.read_excel(StartupFile)
	return df_Init
	#df_Init.to_excel(path, index=False)

DB = 1586
custom_sort = ['No', 'NAME', 'Address Byte', 'Address Bit', 'DataType', 'Log']

DF_DataBase=InitDataFrames(KeyFile)

#DatabaseFiltrado = DF_DataBase[DF_DataBase['Log'] == 1]
print(DF_DataBase)

dimension = DF_DataBase['No'].count()

if dimension > 10:
	Print("Error, You have more than 10 Variables Actives for Log")	
	#print(dimension)

#ExctractDF = DatabaseFiltrado[custom_sort]

Reg1_Name = int(DF_DataBase.iloc[0,2])
print(Reg1_Name)

#DF_DataBase.drop(DF_DataBase.index[0:2],0,inplace=True)
dfnew = DF_DataBase.iloc[5:] # Seleccion de Rows
print(DF_DataBase)
print(dfnew)


dictest = {0:[3,"Tabla 3"], 1:[4,"Tabla 4"], 2:[5,'Tabla 5']}
dictest2 = dictest[0]
print(dictest2[1])


dfnew.to_csv('C:\\Users\\admin\\Desktop\\McSIM\\file_nametest.csv',sep=';', index=False , encoding='utf-8')


'''
TAGName = ExctractDF.iloc[0,1]
print(TAGName)
AddressBYTE_1 = int(ExctractDF.iloc[0,2])
print(AddressBYTE_1)
1_AddressBIT = int(ExctractDF.iloc[0,3])
print(1_AddressBIT)
1_DataTYPE = (ExctractDF.iloc[0,4])
print(1_DataTYPE)


2TAGName = ExctractDF.iloc[1,1]
print(2TAGName)
2AddressBYTE = int(ExctractDF.iloc[1,2])
print(2AddressBYTE)
2AddressBIT = int(ExctractDF.iloc[1,3])
print(2AddressBIT)
2DataTYPE = (ExctractDF.iloc[1,4])
print(2DataTYPE)


3TAGName = ExctractDF.iloc[2,1]
print(3TAGName)
3AddressBYTE = int(ExctractDF.iloc[2,2])
print(3AddressBYTE)
3AddressBIT = int(ExctractDF.iloc[2,3])
print(3AddressBIT)
3DataTYPE = (ExctractDF.iloc[2,4])
print(3DataTYPE)


4TAGName = ExctractDF.iloc[3,1]
print(4TAGName)
4AddressBYTE = int(ExctractDF.iloc[3,2])
print(4AddressBYTE)
4AddressBIT = int(ExctractDF.iloc[3,3])
print(4AddressBIT)
4DataTYPE = (ExctractDF.iloc[3,4])
print(4DataTYPE)


5TAGName = ExctractDF.iloc[4,1]
print(5TAGName)
5AddressBYTE = int(ExctractDF.iloc[4,2])
print(5AddressBYTE)
5AddressBIT = int(ExctractDF.iloc[4,3])
print(5AddressBIT)
5DataTYPE = (ExctractDF.iloc[4,4])
print(5DataTYPE)


6TAGName = ExctractDF.iloc[5,1]
print(6TAGName)
6AddressBYTE = int(ExctractDF.iloc[5,2])
print(6AddressBYTE)
6AddressBIT = int(ExctractDF.iloc[5,3])
print(6AddressBIT)
6DataTYPE = (ExctractDF.iloc[5,4])
print(6DataTYPE)


7TAGName = ExctractDF.iloc[0,1]
print(7TAGName)
7AddressBYTE = int(ExctractDF.iloc[0,2])
print(7AddressBYTE)
7AddressBIT = int(ExctractDF.iloc[0,3])
print(7AddressBIT)
7DataTYPE = (ExctractDF.iloc[0,4])
print(7DataTYPE)


8TAGName = ExctractDF.iloc[0,1]
print(8TAGName)
8AddressBYTE = int(ExctractDF.iloc[0,2])
print(8AddressBYTE)
8AddressBIT = int(ExctractDF.iloc[0,3])
print(8AddressBIT)
8DataTYPE = (ExctractDF.iloc[0,4])
print(8DataTYPE)


9TAGName = ExctractDF.iloc[0,1]
print(9TAGName)
9AddressBYTE = int(ExctractDF.iloc[0,2])
print(9AddressBYTE)
9AddressBIT = int(ExctractDF.iloc[0,3])
print(9AddressBIT)
9DataTYPE = (ExctractDF.iloc[0,4])
print(9DataTYPE)


10TAGName = ExctractDF.iloc[0,1]
print(10TAGName)
10AddressBYTE = int(ExctractDF.iloc[0,2])
print(10AddressBYTE)
10AddressBIT = int(ExctractDF.iloc[0,3])
print(10AddressBIT)
10DataTYPE = (ExctractDF.iloc[0,4])
print(10DataTYPE)


'''

#print(Name)