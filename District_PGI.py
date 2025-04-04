#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('A:\jmk project and study\Data visualiztaion in Excel Project\Data set for project\District_PGI_Table_1.csv')
df.info(),df.head()
df


# In[3]:


df.columns,df.dtypes


# In[4]:


missing_data = df.isnull()
missing_datanotnull = df.notnull()
print(missing_data)


# In[5]:


df.describe()


# In[6]:


headers = ["SI.NO", "STATE","DISTRICT", "GRADE","OVERALL PERFORMANCE","LOQ", "ECT","IF&SE","SS&CP","DL","GP"]
print(headers)


# In[7]:


df.columns = headers
df


# In[8]:


# counvet data types 
df.dtypes
df = df.astype({'STATE' : 'str','DISTRICT' : 'str', 'GRADE' : 'str'})
df.info()


# In[9]:


df_tamil = df[(df['STATE'] == 'Tamilnadu')]
df_tamil.describe


# In[10]:


state_tamilnadu = df[(df['STATE'] == 'Tamilnadu')]
state_chennai = df[(df['DISTRICT'] == 'Chennai')]
print(state_tamilnadu)
state_chennai


# In[11]:


#calculate average overall score by state 1
state_avg_score = df.groupby('STATE')['OVERALL PERFORMANCE'].mean().sort_values(ascending = False)
Top_avg = state_avg_score.head(10)
Bottom_avg = state_avg_score.tail(10)
print("Top 5 performing state")
print(Top_avg)
print("\nBottom 5 performing state")
print(Bottom_avg)



# In[12]:


# calculate correlation with overall score 2
category_correlation = df[['OVERALL PERFORMANCE', 'LOQ',
       'ECT', 'IF&SE', 'SS&CP', 'DL', 'GP']].corr()['OVERALL PERFORMANCE'].sort_values(ascending = False)
print("correlation with overall score")
print(category_correlation)


# In[13]:


df['STATE']


# In[14]:


# Groupby Grade and calculate descriptive statistices for overall performancens 3
grade = df["GRADE"].value_counts()
grade_state = df.groupby ('GRADE')['OVERALL PERFORMANCE'].describe()
over_perform = df['OVERALL PERFORMANCE']
print('overall score statistics of Grade')
print(grade_state)
over_perform


# In[15]:


# hight performance 4 

hight_performance = df[df["GRADE"] == "Uttam"] ["STATE"].value_counts()
print("This State is the consistently Hight-Performance districts\n")
print(hight_performance)


# In[16]:


# calculate standard deviation for category : 5
category_std = df[['LOQ','ECT', 'IF&SE', 'SS&CP', 'DL', 'GP']].std().sort_values(ascending = False)
print(category_std)


# In[17]:


# Visualization for all Querys
# 1 Calculation of Top & Bottom Performance of District :

combine_state = pd.concat([Top_avg,Bottom_avg])
plt.figure(figsize=(8,8))
sns.barplot(x=combine_state.index, y=combine_state.values, palette='viridis')
plt.title('Top & Bottom state of Overall performance')
plt.xlabel('state')
plt.ylabel('overall Performance')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()



# In[18]:


# 2 calculate the correlation of Overall Performance :

plt.figure(figsize=(10,8))
sns.barplot(x=category_correlation.index, y=category_correlation.values, palette='coolwarm')
plt.title('category correlation by overall performance')
plt.xlabel('category')
plt.ylabel('category correlation')
plt.xticks(rotation=50,ha='right')
plt.tight_layout()
plt.show()


# In[19]:


# 3 Groupby Grade and Calculate descritive statisices for overall performance : 

#grade= df["GRADE"].unique()
#print(grade)

plt.figure(figsize=(12,5))
sns.boxplot(x='GRADE', y='OVERALL PERFORMANCE',data=df,order=['Ati-Uttam', 'Uttam', 'Prachesta-1', 'Prachesta-2', 'Prachesta-3', 'Akanshi-1'])
plt.title('Distribution of Overall Performance Score by Grade ')
plt.xlabel('Grade')
plt.ylabel('overall performance')
plt.show()


# In[20]:


# 4 Calculate the Hight Performances State

plt.figure(figsize=(12,8))
hight_performance.sort_values().plot(kind='barh',color='skyblue')
plt.title('Hight Performance State')
plt.ylabel('state')
plt.xlabel('district names')
plt.show()


# In[21]:


# 5 Calulate standard deviation of category

plt.figure(figsize=(12,8))
sns.barplot(x=category_std.index, y=category_std.values, palette='viridis')
plt.title('Standard Deviation of Score Across Categories')
plt.xlabel('categoty')
plt.ylabel('standard deviation')
#plt.xticks(rotation=45,ha='right')
#plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




