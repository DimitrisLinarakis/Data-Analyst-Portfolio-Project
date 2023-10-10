# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:44:19 2023

@author: jimar
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transforrm to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the puprose column 
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualIncome'] = income

#applying for loops to loan data
#using first 10
ficocat = []
length = len(loandata)

for x in range(0,length):
    category = loandata['fico'][x]

    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
       cat = 'Unknown'
        
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.col as conditional statements
#df.loc[df[column_name] condition, new_column_name] = 'value if the condition is met'

#for interest rates, a new column is wanted. Rate > 0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate,type'] = 'high'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate,type'] = 'low'

#numbers of loans/rows by fico.category
catplot = loandata.groupby(loandata['fico.category']).size()
catplot.plot.bar(color = 'red', width = 0.2)

#figure attributes
plt.title('Fico Category vs Borrowers')
plt.xlabel('Fico Category')
plt.ylabel('Number of Borrowers')
plt.show()

#numbers of loans/rows by purpose
purplot = loandata.groupby(loandata['purpose']).size()
purplot.plot.bar(color = 'grey')

#figure attributes
plt.title('Purpose of Loan vs Borrowers')
plt.xlabel('Purpose')
plt.ylabel('Number of Borrowers')
plt.show()

#Building scatter plots
#DTI number is one way lenders measure your ability to manage 
#the monthly payments to repay the money you plan to borrow.
plt.scatter(x = loandata['dti'], y = loandata['annualIncome'])
plt.title('Distribution of DTI per Annual Income')
plt.xlabel('DTI')
plt.ylabel('Annual Income')
plt.show()

#seaborn usage / Plot income vs dti using seaborn
sns.regplot(x = 'dti', y = 'annualIncome', data = loandata, scatter_kws = {"color": "red"}, line_kws = {"color": "blue"})

#exporting data to csv
loandata.to_csv('loan_cleaned.csv', index = True)




















