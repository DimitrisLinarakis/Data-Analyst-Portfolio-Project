# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:22:02 2023

@author: jimar
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') --> format
data = pd.read_csv('transaction2.csv', sep=';')

# summary of the data
data.info()

# working with the calculations

# Defining variables
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
SellingPricePerItem = data['SellingPricePerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#Mathematical Operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

#--------------------------------------------------------------

CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#--------------------------------------------------------------

#Adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup Calculation = (Sales - Cost)/Cost
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Drop an extra column that occured
#data = data.drop(columns=['MarkupPerTransaction'])

#round values in 'Markup' column to two decimal places
data['Markup'] = data['Markup'].round(2)

#Alternative way of rounding 'Markup'
#data['Markup'] = round(data['Markup'],2)

#typeCast 
day = data['Day'].astype(str)

year = data['Year'].astype(str)

#combine 3 columns to 1, so as date to be in a readable format
data['correctDate'] = day + '-' + data['Month'] + '-' + year

#using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #views the first 3 rows
data.iloc[-5:] #views the last 5 rows

data.head() #by default returns the first 5 rows
data.iloc[:,2] #views all rows - column with index = 2
data.iloc[4,2] #views specific value

#using split to split the client's keywords field
#new_var = column.str.split('sep' , expand = True) ---> splits every single comma, not only the first one
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keyword
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#drop the brackets, replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on ='key')
data = pd.merge(data, seasons, on= 'Month')

#Drop extra columns from the dataset
data = data.drop(columns=['ClientKeywords'])

data = data.drop(columns=['Day'])
data = data.drop(columns=['Month'])
data = data.drop(columns=['Year'])

#alternative way to drop columns 
#data = data.drop(columns=['Day','Month','Year'])

#Export into a csv file
data.to_csv('ValueInc_Cleaned.csv', index = False)


















































