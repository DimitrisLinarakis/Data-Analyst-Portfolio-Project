# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:22:32 2023

@author: jimar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#calculating the number of articles have been written per author 
data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop(columns = ['engagement_comment_plugin_count'])
    
#creating a keyword flag
keyword = 'crash'

#creating a function
def keywordflag(keyword):
    
    length = len(data)
    keyword_flag = []

    for x in range(0,length):
        heading = data['title'][x]
        
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)  
    return keyword_flag

keywordflag = keywordflag('murder')

#creating a new column in data dataframe
keywordflag = pd.Series(keywordflag)
data['keyword_flag'] = keywordflag

#SentimentIntensityAnalyzer 
sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

#creating 3 new colums in data dataframe
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#exporting the data 
data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)























































