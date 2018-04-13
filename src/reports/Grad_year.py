import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

students=pd.read_csv('student.csv')
students.sort_values("StudID", inplace=True)

def fin_grad_year():
    values=students['Graduate'].value_counts().tolist()
    #years = grades[keys]["Year"].tolist()
    years_list_0 = students['Graduate'].tolist()#[2011,2012,2013,2014]
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


years,values=fin_grad_year()
