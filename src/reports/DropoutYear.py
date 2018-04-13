
# coding: utf-8

# In[19]:


import csv
import pandas as pd
import matplotlib.pyplot as plt

students=pd.read_csv('student.csv')
students.sort_values("StudID", inplace=True)
#years=students.groupby(['Leave'])['Leave'].count()
#years

#list=student.tolist()
#list
student=students.Leave.value_counts()
student

def fin_drop_year():
    values=students.groupby('Leave')['Leave'].count().tolist()
    #years = grades[keys]["Year"].tolist()
    years_list_0 = students['Leave'].tolist()#[2011,2012,2013,2014]
    years_set = set(years_list_0)
    years_list = list(years_set)
    num_kind = type(years_list[-1])
    filter_f = lambda x : type(x) == num_kind
    years_list_filtered = filter(filter_f, years_list)
    years_list_filtered = sorted(years_list_filtered)
    years_list_filtered = [years_list_filtered for years_list_filtered in years_list_filtered if str(years_list_filtered) != 'nan']
    new=[]
    for item in years_list_filtered:
        new.append(int(item))
    return new, values


years,values=fin_drop_year()


