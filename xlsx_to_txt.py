# coding: utf-8
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from string import digits
import numpy as np
import tkinter as tk
from tkinter import filedialog

root  = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)


df = pd.read_excel(file_path, sheet_name ='Sheet1', header=0)

f = open("WalidProjet.txt", "a", encoding="utf-8")


for i in range(len(df.columns)) :
	if i < len(df.columns) - 1 :
		f.write(df.columns[i])
		f.write(";")
	else : f.write(df.columns[i])

f.write("\n")


for j in range(len(df['"Id"'])) :
	for i in range(len(df.columns)) :
		if pd.notna(df[df.columns[i]][j]) :
			if i < len(df.columns) - 1 :
				f.write(str(df[df.columns[i]][j]))
				f.write(";")
			else : f.write(str(df[df.columns[i]][j]))

		elif pd.isna(df[df.columns[i]][j]) :
			if i < len(df.columns) - 1 :
				f.write("")
				f.write(";")
			else : f.write("")
			
	f.write("\n")

f.close()