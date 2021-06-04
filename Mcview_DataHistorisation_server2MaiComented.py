#!/usr/bin/env python
import os
import requests
import json
import pprint
import pandas as pd 
import numpy as np
from datetime import datetime
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Functions ----------------------------------------------------------------------------

def Insert_DF_inGsheets(gsheetindex,df):        # Function for write inside GSpread Sheet.
	Name = sh.get_worksheet(gsheetindex)        #-> 0 - first sheet, 1 - second sheet etc.
	your_dataframe = pd.DataFrame(df)           # Create Variable Type Data Frame 
	set_with_dataframe(Name, your_dataframe)    #-> THIS EXPORTS YOUR DATAFRAME TO THE GOOGLE SHEET (Tab Name, DataFrame)


def Read_DF_inGsheets(gsheetindex):             # Function for READ inside GSpread Sheet.
	Name = sh.get_worksheet(gsheetindex)        #-> 0 - first sheet, 1 - second sheet etc.	
	Table = Name.get_all_records()              # Get all Data from selected Tab.
	dfRead = pd.DataFrame(Table)                # Copy Data in DF Read.
	return dfRead                               # Return Variable.
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Global Variables Definition ---------------------------------------------------------

global HRSCNRstatus
global HRS1SMTAGstatus
global HRSH2Mstatus
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Json Key for Data Analysis Credentials ----------------------------------------------

gc = gspread.service_account(filename="mcview-starter-kit.json")     # Json File for Google oauth2client Service Account Credentials.
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Initial Values Declaration ----------------------------------------------------------

MoreNewData = 0
HRSCNRstatus = 0
HRS1SMTAGstatus = 0
HRSH2Mstatus = 0
LoopApi = 0
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Mcview Tag Id :[GoogleSheets,NameTab,Tag Description]
#df = pd.read_excel(r'C:\Users\admin\Desktop\Mycode\McView Exchange Table_ HRSRouen.xlsx', sheet_name ='in', header=0)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
IDsGsheet = {1:[1,"ALM_MOT","Mot contenant les alarmes"],
2:[99,"DEF_S1_KO","Alarme alimentation cadre source 1"],
3:[2,"Code_Acces","Code accès pour lancer un remplissage d\'un véhicule"],
4:[99,"DEF_AU","Défaut arret urgence"],
5:[99,"DEF_C1","Défaut moteur du compresseur H2 C1"],
6:[99,"DEF_C10","Défaut moteur du compresseur d\'air comprimé C10"],
7:[99,"DEF_C2","Défaut moteur C2"],
8:[99,"DEF_CHUTEP","Défaut chute de pression intempestive"],
9:[99,"DEF_DELTAP","Défaut contrôle delta P (étanchéité du flexible au démarrage d\'un remplissage <= 2barg)"],
10:[3,"DEF_MOT","DEFAUTS GENERAL"],
11:[99,"DEF_PT21B","DEFAUT PRESSION BASSE AMONT COMPRESSEUR"],
12:[99,"DEF_PT21H","Défaut pression haute en amont du compresseur H2 (>=200barg)"],
13:[99,"DEF_PT22H","Défaut pression haute en aval du compresseur H2 (>=430 barg)"],
14:[99,"DEF_S_KO","Défaut Stockages internes et sources externes épuisées"],
15:[4,"GC01","Concentration de l\'H2 en  pourcentage la LIE"],
16:[5,"MOP_L1","Messages opérateur ligne 1"],
17:[6,"MOP_L2","Message opérateur ligne 2"],
18:[7,"MOP_L3","Message opérateur ligne 3"],
19:[8,"Source1","Pression de la source 1 (barg)"],
20:[9,"PT10","Pression air comprimé (barg)"],
21:[10,"PT2-1","Pression en amont du compresseur (barg)"],
22:[11,"PT2-2","Pression en aval du compresseur (barg)"],
23:[12,"PT3-1","Pression stockage interne N°1"],
24:[13,"PT3-2","Pression Stockage interne N°2"],
25:[14,"PT4","Pression du réservoir du client (barg)"],
26:[15,"SP_PR","Recopie de la consigne du détendeur pneumatique (en barg)¶"],
27:[16,"TT-Ext","Température ambiante (°C)"],
28:[99,"secondes",""],
29:[17,"Source2","PT1-2 pression de la source externe n°2 (en barg)"],
30:[18,"DEBIT_INST","Débit instantané (g/s)"],
31:[19,"MASSE_CUMULEE","Totalisateur en (Kg)"],
32:[20,"MASSE_RECHARGE","Masse par recharge (en Kg)"],
33:[99,"VIEWON_DEF","pour afficher l\'état de la station sur viewon"],
34:[99,"VIEWON_PV_PR","permet de convertir des volt en barg dans viewon"],
35:[99,"VIEWON_SENDMAIL",""],
36:[99,"VIEWON_SP_PR","permet de convertir des Vdc en barg dans viewon"],
37:[21,"PT10-SFC",""],
38:[22,"PT3-2-SFC",""],
39:[23,"P1-finale","pression finale de la dernière recharge"],
40:[24,"DEF_MOT2","DEFAUTS LIES A LA COMPRESSION"],
41:[99,"DEF_FEU","DEFAUT FLAMMES DETECTEES"],
42:[99,"DEF_DFLAM","ALERTE DYSFONCTIONNEMENT DETECTEUR FLAMMES"],
43:[99,"DEF_DGAZ","ALERTE DYSFONCTIONNEMENT DETECTEUR GAZ"],
44:[99,"DEF_GAZ25","DEFAUT NIVEAU GAZ 25% LIE - ARRET D\'URGENCE"],
45:[99,"DEF_PT11","DEFAUT CAPTEUR PT1.1"],
46:[99,"DEF_PT12","DEFAUT CAPTEUR PT1.2"],
47:[99,"DEF_PT13","DEFAUT CAPTEUR PT1.3"],
48:[99,"DEF_PT31","DEFAUT CAPTEUR PT3.1"],
49:[99,"DEF_PT32","DEFAUT CAPTEUR PT3.2"],
50:[99,"DEF_PT10","DEFAUT CAPTEUR PT10"],
51:[99,"DEF_AIR_COMP","DEFAUT AIR COMPRIME"],
52:[99,"DEF_TEMP_EXT","DEFAUT TEMPERATURE AMBIANTE"],
53:[99,"DEF_PT21","DEFAUT CAPTEUR PT2.1"],
54:[99,"DEF_PT22","DEFAUT CAPTEUR PT2.2"],
55:[99,"DEF_MEMB_C21","DEFAUT MEMBRANE COMPRESSEUR C2.1"],
56:[99,"DEF_MEMB_C22","DEFAUT MEMBRANE COMPRESSEUR C2.2"],
57:[99,"DEF_OIL_C21","DEFAUT PRESSION HUILE COMPRESSEUR C2.1"],
58:[99,"DEF_OIL_C22","DEFAUT PRESSION HUILE COMPRESSEUR C2.2"],
59:[99,"DEF_CHILLER","DEFAUT CHILLER"],
60:[99,"DEF_PT31HAUT","DEFAUT PRESSION HAUTE STOCKAGE 1"],
61:[99,"DEF_PT32HAUT","DEFAUT PRESSION HAUTE STOCKAGE 2"],
62:[99,"DEF_PSHH2HAUT","DEFAUT PRESSION SECURITE HAUTE PSHH2"],
63:[99,"DEF_FLEX_H","DEFAUT PRESSION FLEXIBLE ELEVEE"],
64:[99,"DEF_PT4","DEFAUT CAPTEUR PT4"],
65:[99,"DEF_20G_S","DEFAUT DEBIT HAUT"],
66:[99,"DEF_PSHH4HAUT","DEFAUT PRESSION SECURITE HAUTE PSHH4"],
67:[99,"DEF_S2_KO","ALERTE ALIMENTATION CADRE SOURCE 2"],
68:[99,"DEF_S3_KO","ALERTE ALIMENTATION CADRE SOURCE 3"],
69:[99,"DEF_GAZ10","ALERTE NIVEAU GAZ 10% LIE"],
70:[99,"DEF_T_C1","ALERTE TEMPERATURE COMPRESSEUR C1"],
71:[99,"DEF_T_C2","ALERTE TEMPERATURE COMPRESSEUR C2"],
72:[99,"DEF_PT10H","ALERTE PRESSION SOURCE(S) ELEVEE(S)"],
73:[25,"DEF_MOT1","DEFAUTS LIES A LA DISTRIBUTION"],
74:[26,"Cons-PCV4","consigne du pcv4 en barg"],
75:[99,"Test_sms_THT",""],
76:[99,"Test_sms_THT_Grp",""],
79:[27,"Pveh","pression véhicule (en barg)"],
80:[28,"Tveh","Température vehicule"],
81:[29,"Tsortie_comp","température sortie compresseur"],
82:[30,"Tdistrib","Température de distribution"],
83:[31,"Tdetect_incendie","température détection incendie zone compression (en°C)"],
84:[99,"DEF_GC01_filtre",""],
85:[99,"Seuil_Anticipation",""],
86:[99,"Seuil_Source1_ok",""],
87:[99,"Seuil_Source2_ok",""],
88:[99,"Seuil_PT1_KO",""],
89:[99,"Flag_Def_S1_KO",""],
90:[99,"Flag_Def_S2_KO",""],
91:[99,"GC01_filtre",""],
92:[99,"unlock_HRS","Signal permettant de débloquer la station via un système extérieur (ex FillnDrive) (1= déblocage de la station)"],
93:[99,"GSM_LEV","niveau de la 3G"],
94:[32,"COM-VCHSS","Volume du réservoir véhicule selon SAEJ2799 (M3)"],
95:[99,"test",""],
96:[99,"unlock",""],
97:[33,"Valeur_P0","Valeur P0 selon SAEJ-2601 (bar)"],
98:[34,"Mem_P_INIT_V0","Mémoire pression initial V0 selon SAEJ-2601(bar)"],
99:[35,"Mem_P_Finale_V0","Mémoire pression finale V0 selon SAEJ-2601(bar)"],
100:[36,"Cpt_Masse_H2","Compteur masse H2 V0 selon SAEJ-2601"],
101:[37,"APRR","Valeur Calculée APRR selon SAEJ-2601 (bar/min)"],
102:[38,"PTarget","Valeur calculée PTarget selon SAEJ-2601 (bar)"],
103:[39,"Valeur_V0","Valeur calculée V0 selon SAEJ-2601 (l)"],
104:[40,"CPT_deb_nul","Compteur débit nul selon SAEJ-2601 (l)"],
105:[99,"DEF_T_HYCOMP","DEFAUT TEMPERATURE HAUTE GAZ SORTIE COMPRESSEUR"],
106:[99,"DEF_CORRIDOR","DEFAUT PRESSION EN DEHORS DU CORRIDOR THEORIQUE DE DISTRIBUTION"],
107:[99,"DEF_CPT_DEBMASS_V0","DEFAUT COMPTAGE IMPULSION DEBIMETRE MASSIQUE LORS DU CALCUL V0"],
108:[99,"DEF_CPT_PAUSEDEB","DEFAUT NOMBRE DE PAUSE DE DEBIT SUPERIEURES A 10 PENDANT DISTRIBUTION"],
109:[41,"ManC10","commande manuelle moteur C10"],
110:[42,"ManC21","commande manuelle moteur C2"],
111:[43,"ManGF","commande manuelle  Chiller"],
112:[44,"ManVFC1-1","commande manuelle VFC1-1"],
113:[45,"ManVFC1-2","commande manuelle VFC1-2"],
114:[46,"ManVFC2-1","commande manuelle VFC2-1"],
115:[47,"ManVFC2-2","commande manuelle VFC2-2"],
116:[48,"ManVFC2-3","commande manuelle VFC2-3"],
117:[49,"ManVFC3-1","commande manuelle VFC3-1"],
118:[50,"ManVFC3-2","commande manuelle VFC3-2"],
119:[51,"ManVFC4-1","commande manuelle VFC4-1"],
120:[52,"ManVFC4-2","commande manuelle VFC4-2"],
121:[53,"Mode_Manuel","activer le mode manuel"]}


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

while True:     # Main Program LOOP

	# HRS Rouen
	try:

		# -x-x-x-x-x-x-x-x--x-x-x-x-x--x-x-x-x-x-x-  HRS Rouen -x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x
		#----Obtain las Transaction ID  -------------------------------------------------------------------------------
		sh = gc.open_by_key('10Ik_0gKeW-_rbwFFTn8e2xhtpL_wFAvtEZj4AVFkc4Q')     # HRS Rouen- Gsheet ApiKey. 
		Transactionsheet = sh.get_worksheet(0)                                  # Open Tab 0 From Speadsheet choosed.
		StartingTransactionID = Transactionsheet.cell(1,2).value                # Get Value from SpreadSheet Tab 0 Cells (1,2)
		LastTransactionSTR = str(StartingTransactionID)                         # Convert to value to type String.

		#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

		# First CALL APIs Datamailbox & Google  -------------------------------------------------------------------------------

		# Sync DATA POST
		Authentication = {'t2mdevid': '87e76678-d393-4bdc-88a4-08cf164b4944','t2mtoken': 'w0DRk9x2GuYXOERMAUUUNc0PDaJRI6Xf0CkDgGbjSONvx5ilQA', 'createTransaction':'true','lastTransactionId':LastTransactionSTR}
		respuesta = requests.post('https://data.talk2m.com/syncdata', data=Authentication)      # Ewon API Datamailbox Request.
		respuestajson = respuesta.json()        # Save all Data (Json Request) 
		TotalDimension = 0                      # Re-initialize TotalDimension Variable.

		print('-----------------------------------')
		print('McView Data Historisation Service')
		print('-----------------------------------')
		#Transaction ID Data mailbox
		TransactionID = respuestajson.get('transactionId')          # Get new Tansaction ID from the ewon API request.
		LastTransactionSTR = str(TransactionID)                     # Convert Variable to String
		print('Transaction ID: ' + str(TransactionID))				# Print Variable
		Transactionsheet = sh.get_worksheet(0)						# Select Spread sheet Tab
		Transactionsheet.update_cell(1,2, TransactionID)			# Write in Spread sheet Tab 0 cell 1,2 -- New transaction Number

		#Flag.. More Data Available?
		FLAGMoreData = respuestajson.get('moreDataAvailable')	    # If There is a new packet to call, moreDataAvailable = 1 if no = 0
		print('More Data Available: ' + str(FLAGMoreData))			# print Variable
		if FLAGMoreData == True:									# IF Previous Tag = 1, we set Internal Tag "MoreNewData" to 1
			MoreNewData = 1											# Set tag "MoreNewData" to 1
		#Ewon tags inside Reponse 
		ewonTags = respuestajson.get('ewons')[0].get('tags')		# Select Ewon To Grab Data... This is Always 0 since we have 1 eWon per HRS
		range_ewontagsinResponse = len(ewonTags)					# Obtain the Lenght of Data inside the Json Package
		contador = range_ewontagsinResponse							# Give Lenght Value to tag "Contador" 
		print('Response Lenght: '+ str(range_ewontagsinResponse))	# print Lenght of Data inside Json Package
		print('-----------------------------------')				# print Separation Lines
		print('\n')													# print Jump Line


		for x in range(0,range_ewontagsinResponse):					# For LOOP from 0 to Lenght of Data Recived inside Json Package
			sleep(2.5)												# Sleep 2.5 sec
			print('--------------------')							# print Jump Line
			ix = respuestajson.get('ewons')[0].get('tags')[x]		# ix --> store Tag X from ewon 0 
			print('\n')												# print Jump Line
			Mcview_TagID = ix['ewonTagId']							# Set eWon TAGID to "McView_TagID" Variable... This will Help to identify it from our Exchange Table.
			print('Mcview TagID: ' + str(Mcview_TagID))				# print Variable "Mcview TagID"
			print('Loop #: ' + str(contador))						# Prin value from our FOR LOOP

			#### --- availability Report --- ####
			if Mcview_TagID == 417:
				HRSCNRstatus = ix['value']
				

			if 'history' in ix:

				IDArray = IDsGsheet[Mcview_TagID]		# Read Array Id MCview
				IndexNumber = IDArray[0]				# Read Index Number ID
				TabName_Gsheet = IDArray[1]				# Read Tab name Id Mcview         
				DescriptionTag = IDArray[2]				# Read Description Tag

				newdata = ix['history']
				dfbrut = pd.DataFrame(newdata)
				df = dfbrut.loc[:,['value', 'date']]
				df['TagId'] = Mcview_TagID
				df['date'] = pd.to_datetime(df.date)
				df['Hour'] = df.date.dt.hour
				df['Month'] = df.date.dt.month
				df['Tagname'] = TabName_Gsheet
				df['Extrainfo'] = DescriptionTag
				
				df.rename(columns = {'value':'Value'}, inplace=True)
				df.rename(columns = {'date':'TimeStr'}, inplace=True)
				custom_sort = ['Value', 'TimeStr', 'TagId', 'Hour', 'Tagname', 'Month','Extrainfo']


				print('Index #: ' + str(IndexNumber))

				if IndexNumber != 99:

					Step1 = 0
					while Step1 == 0:
						try:
							df_histo = Read_DF_inGsheets(IndexNumber)
							Step1 = 1
						except:
							print("Step 1 Error: Reading Spread Default HRS-Rouen")
							sleep(5)

					Dfsize = df_histo.size
					RowNumbers = df_histo['Value'].count()
					RowsToDelete = RowNumbers * 0.8
					IntRowsToDelete = int(RowsToDelete)
					print('Row Size: ' + str(RowNumbers))
					print('Rows to delete (80%): ' + str(IntRowsToDelete))
					TotalDimension = TotalDimension + Dfsize
					Percentage_Dfsize = (Dfsize/63000)*100
					Percentage_TotalDimension = (TotalDimension/5000000)*100
					print('Database Dimension: '+ str(Percentage_Dfsize) + ' %') # 66,666
					print('Total Cells used:' + str(Percentage_TotalDimension) + ' %') # 5,000,000
					sleep(3)


					if Percentage_Dfsize > 95:
						dfbackup = df_histo.iloc[:4999] #Select The Rows to Save.
						dfMaster = pd.read_csv('/home/pi/Desktop/Mcview/HRS-Rouen/' + TabName_Gsheet + '.csv' , sep=';')
						dfnewMaster = pd.concat([dfMaster,dfbackup])
						dfnewMaster.to_csv('/home/pi/Desktop/Mcview/HRS-Rouen/' + TabName_Gsheet + '.csv' ,sep=';', index=False , encoding='utf-8')

						dfsave = df_histo.iloc[5000:]	#Select rows from line 7000 and save it.
						
						string_Erase = TabName_Gsheet + '!A2:G10000'
						# sh.values_clear('PT STK 2!A2:B3') --- < Example
						sh.values_clear(string_Erase)
						
						#After clearing Cells in google Sheet, we concatenate our 2 DF for post it.
						
						df_Concatenate = pd.concat([dfsave,df])
						df_Concatenate[custom_sort]

						Step2 = 0
						while Step2 == 0:
							try:
								Insert_DF_inGsheets(IndexNumber,df_Concatenate)
								Step2 = 1
							except:
								print("Step 2 Error: Writing Spread Default HRS-Rouen")
								sleep(5)

					if Percentage_Dfsize <= 95:
						df_Concatenate = pd.concat([df_histo,df])
						df_Concatenate[custom_sort]

						Step2 = 0
						while Step2 == 0:
							try:
								Insert_DF_inGsheets(IndexNumber,df_Concatenate)
								Step2 = 1
							except:
								print("Step 2 Error: Writing Spread Default HRS-Rouen")
								sleep(5)

					print(df)		# Print Data Frame to Historized.
					sleep(2.5)		# Wait 2.5 sec


			contador = contador - 1
			print('--------------------')
			print('\n')

		#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


		# More Data LOOP -------------------------------------------------------------------------------

		### More Data Available
		while MoreNewData == 1:
			TotalDimension = 0
			print("Waiting for the New Request....")
			sleep(100) #esperando 1 min 10 segundos para el siguiente request
			
			

			Authentication = {'t2mdevid': '87e76678-d393-4bdc-88a4-08cf164b4944','t2mtoken': 'w0DRk9x2GuYXOERMAUUUNc0PDaJRI6Xf0CkDgGbjSONvx5ilQA', 'createTransaction':'true','lastTransactionId':LastTransactionSTR}
			respuesta = requests.post('https://data.talk2m.com/syncdata', data=Authentication)
			respuestajson = respuesta.json()


			print('-----------------------------------')
			print('McView Data Historisation Service')
			print('-----------------------------------')
			#Transaction ID Data mailbox
			TransactionID = respuestajson.get('transactionId')
			LastTransactionSTR = str(TransactionID)
			print('Transaction ID: ' + str(TransactionID))
			Transactionsheet = sh.get_worksheet(0)
			Transactionsheet.update_cell(1,2, TransactionID)

			#Flag.. More Data Available?
			FLAGMoreData = respuestajson.get('moreDataAvailable')
			print('More Data Available: ' + str(FLAGMoreData))

			#Ewon tags inside Reponse 

			ewonTags2 = respuestajson.get('ewons')[0].get('tags')
			range_ewontagsinResponse = len(ewonTags2)
			contador = range_ewontagsinResponse
			print('Response Lenght: '+ str(range_ewontagsinResponse))
			print('-----------------------------------')
			print('\n')


			for x in range(0,range_ewontagsinResponse):
				sleep(2.5)
				print('--------------------')
				ix = respuestajson.get('ewons')[0].get('tags')[x]
				print('\n')
				Mcview_TagID = ix['ewonTagId']
				print('Mcview TagID: ' + str(Mcview_TagID))
				print('Loop #: ' + str(contador))

				#### --- availability Report --- ####
				if Mcview_TagID == 417:
					HRSCNRstatus = ix['value']

				
				if 'history' in ix:

					IDArray = IDsGsheet[Mcview_TagID]		# Read Array Id MCview
					IndexNumber = IDArray[0]				# Read Index Number ID
					TabName_Gsheet = IDArray[1]				# Read Tab name Id Mcview
					DescriptionTag = IDArray[2]				# Read Description Tag


					newdata = ix['history']
					dfbrut = pd.DataFrame(newdata)
					df = dfbrut.loc[:,['value', 'date']]
					df['TagId'] = Mcview_TagID
					df['date'] = pd.to_datetime(df.date)
					df['Hour'] = df.date.dt.hour
					df['Month'] = df.date.dt.month
					df['Tagname'] = TabName_Gsheet
					df['Extrainfo'] = DescriptionTag
				
				df.rename(columns = {'value':'Value'}, inplace=True)
				df.rename(columns = {'date':'TimeStr'}, inplace=True)
				custom_sort = ['Value', 'TimeStr', 'TagId', 'Hour', 'Tagname', 'Month','Extrainfo']
				print('Index #: ' + str(IndexNumber))

				if IndexNumber != 99:
						
						Step1 = 0
						while Step1 == 0:
							try:
								df_histo = Read_DF_inGsheets(IndexNumber)
								Step1 = 1
							except:
								print("Step 1 Error: Reading Spread Default HRS-Rouen")
								sleep(5)

						Dfsize = df_histo.size 							# Count the Size of the Data frame Cells used in the Tab of Google Sheets.
						RowNumbers = df_histo['Value'].count()			# Count Dataframe's Row #
						RowsToDelete = RowNumbers * 0.8					# Operation to know 80% of the data frame
						IntRowsToDelete = int(RowsToDelete)				# Convert Variable to type "int"
						print('Row Size: ' + str(RowNumbers))		
						print('Rows to delete (80%): ' + str(IntRowsToDelete))
						TotalDimension = TotalDimension + Dfsize
						Percentage_Dfsize = (Dfsize/63000)*100
						Percentage_TotalDimension = (TotalDimension/5000000)*100
						print('Database Dimension: ' + str(Percentage_Dfsize) + " %") #66,666.6
						print('Total Cells used: ' + str(Percentage_TotalDimension) + ' %') #5,000,000
						sleep(3)
						if Percentage_Dfsize > 95:
							dfbackup = df_histo.iloc[:4999] #Select The Rows to Save.
							dfMaster = pd.read_csv('/home/pi/Desktop/Mcview/HRS-Rouen/' + TabName_Gsheet + '.csv' , sep=';')
							dfnewMaster = pd.concat([dfMaster,dfbackup])
							dfnewMaster.to_csv('/home/pi/Desktop/Mcview/HRS-Rouen/' + TabName_Gsheet + '.csv' ,sep=';', index=False , encoding='utf-8')


							dfsave = df_histo.iloc[5000:]	#Select rows from line 7000 and save it.
							string_Erase = TabName_Gsheet + '!A2:G10000'
							sh.values_clear(string_Erase)
							df_Concatenate = pd.concat([dfsave,df])
							df_Concatenate[custom_sort]

							Step2 = 0
							while Step2 == 0:
								try:
									Insert_DF_inGsheets(IndexNumber,df_Concatenate)
									Step2 = 1
								except:
									print("Step 2 Error: Writing Spread Default HRS-Rouen")
									sleep(5)


						if Percentage_Dfsize <= 95:
							df_Concatenate = pd.concat([df_histo,df])
							df_Concatenate[custom_sort]

							Step2 = 0
							while Step2 == 0:
								try:
									Insert_DF_inGsheets(IndexNumber,df_Concatenate)
									Step2 = 1
								except:
									print("Step 2 Error: Writing Spread Default HRS-Rouen")
									sleep(5)

						print(df)
						sleep(2.5)



				contador = contador - 1
				print('--------------------')
				print('\n')
				

			if FLAGMoreData != True:
				MoreNewData = 0

	except:
		print('\n')
		print('Error when establishing the connection with eWon HRS-Rouen')
		MoreNewData = 0
		HRSCNRstatus = 4	# Offline Status
		print('\n')
		pass



	# ---------------------    Wave Exit  ---------------------------
	print('\n')
	LoopApi = LoopApi + 1
	print('------------------------------')
	print('Data Wave #: ' + str(LoopApi))
	print('------------------------------')
	print('\n')

	print('Waiting for next Data Wave...')
	sleep(3600)
	print('Data Wave will start in 5 min')
	sleep(120)
	print('Data Wave will start in 3 min')
	sleep(120)
	print('Data Wave will start in 1 min')
	sleep(60)
	print('Data Wave Initialization')
	emailAlertMEMO = 0
	# #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
