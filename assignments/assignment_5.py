'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''
#Your code here:

import csv
import pandas as pd
import datetime 
import numpy as np

a = ['_','error','NaN','nan','ERROR']
df = pd.read_csv("attendance_to_clean.csv", na_values= a)

#df.sort_values("NAME_STUDENT", inplace = True)

for index, lines in df.iterrows():
    try:
        a = datetime.datetime.strptime(lines['DATE'], '%Y-%m-%d')
        ff = datetime.datetime(2022,9, 1)
        if a < ff:
            df.loc[index, 'DATE'] = np.nan
        else: 
             continue
    except:
        df.loc[index, 'DATE'] = np.nan

for index, lines in df.iterrows():
    try:
        a = float(lines['COUNT'])
        if a < 10:
            df.loc[index, 'COUNT'] = a
        else :
            df.loc[index, 'COUNT'] = np.nan
    except:
        df.loc[index, 'COUNT'] = np.nan

for index, lines in df.iterrows():
    try:
        b = float(lines['BEGIN_HOUR'])
        if b < 20:
            df.loc[index, 'BEGIN_HOUR'] = b
        else:
            df.loc[index, 'BEGIN_HOUR'] = np.nan
    except:
        df.loc[index, 'BEGIN_HOUR'] = np.nan
        


'''for index, lines in df.iterrows():
    try:
        a = float(lines['WEEK'])
    except:
        df.loc[index, 'WEEK'] = np.nan
df = df[df['WEEK'] < 9]'''


for index, lines in df.iterrows():
    try:
        c = float(lines['WEEK'])
        if c < 9:
            df.loc[index, 'WEEK'] = c
        else:
            df.loc[index, 'WEEK'] = np.nan
    except:
        df.loc[index, 'WEEK'] = np.nan

for index, lines in df.iterrows():
    if str(lines['NAME_STUDENT'])[0].isalpha() == True:
        continue
    else:
        df.loc[index, 'NAME_STUDENT'] = np.nan
        
df.dropna(inplace=True)
df.drop_duplicates(inplace = True) 

df.sort_values(["NAME_STUDENT", 'DATE', 'BEGIN_HOUR', 'WEEK'], inplace = True)
#df.sort_values('NAME_STUDENT', inplace = True)
df = df.reset_index()
del df['index']

print(df)