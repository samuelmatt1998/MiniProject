import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.metrics import confusion_matrix
#import seaborn as sns

df1=pd.read_csv('Eyes-closed-EEG.csv')
df1.dropna(inplace=True)
column_names = df1.columns.tolist()
column_names

rows_to_drop = []  # Initialize a list to store indices of rows to drop

# Iterate through each row
for index, row in df1.iterrows():
  # Check if any value in the row is in the list of column names
  if any(value in column_names for value in row):
    rows_to_drop.append(index)  # Add the index of the row to rows_to_drop list

# Drop the identified rows
rows_to_drop
df1.drop(rows_to_drop, inplace=True)
df1['group_id'] = df1['Group & ID'].str.extract(r'E(\d+)-')

# Displaying the DataFrame with the new 'group_id' column
dfc = df1.iloc[:, 2:]
#Test Data
df1.to_csv('train.csv')
#categories
dfc1=df1.iloc[:319,:]
dfc1.to_csv('group1.csv')

dfc2=df1.iloc[319:616,:]
dfc2.to_csv('group2.csv')

dfc3=df1.iloc[616:,:]
dfc3.to_csv('group3.csv')

# Extracting specified number of rows from each DataFrame
dfc1_sample = dfc1.head(77)  # Extract 63 rows from dfc1
dfc2_sample = dfc2.head(55)  # Extract 59 rows from dfc2
dfc3_sample = dfc3.head(66)  # Extract 61 rows from dfc3

# Concatenate the sampled DataFrames into 'test'
test = pd.concat([dfc1_sample, dfc2_sample, dfc3_sample], ignore_index=True)
test.to_csv('test.csv')

print(df1.shape)
