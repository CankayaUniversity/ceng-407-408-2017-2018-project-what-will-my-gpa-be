
import csv
import pandas as pd



path="datastudent/"
def fin_drop_year(filename):

    students = pd.read_csv(path+filename)
    students.sort_values("StudID", inplace=True)
    values=students.groupby('Leave')['Leave'].count().tolist()
    years_list_0 = students['Leave'].tolist()
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

def get_drop_file(filename):
    if not filename:
        filename="student.csv"
        labels,values=fin_drop_year(filename)
        return labels,values
    else:
        labels,values=fin_drop_year(filename)
        return labels,values


filename=[]
years,values=get_drop_file(filename)



