def get_course_avg(ids, courses, years, letters, course):
    n_records = len(ids)
    letters_set = set(letters)
    #nan_float = 
    stop_grades = set(["S", "U", None, "W"])
    #print(letters_set)
    letters_set = letters_set.difference(stop_grades)
    letters_filtered = list(letters_set)
    del letters_filtered[1]
    letters_filtered = sorted(letters_filtered) 
    print(letters_filtered)
    years_set = set(years)
    years_list = list(years_set)
    print(years_list)
    stat_val = dict()
    for i in range(len(years_list)):
        year = years_list[i]
        stat_val[year] = [0, 0]
    print(stat_val)    
    n_letters = len(letters_filtered)
    #print(letters_set)
    for i in range(n_records):
        if (courses[i] == course):
            year = years[i]
            letter = letters[i]
            if letter in letters_filtered:
                stat = stat_val[year] 
                letter_val = n_letters - letters_filtered.index(letter)
                stat[0] += letter_val
                stat[1] += 1
                stat_val[year] = stat    
                
    
    for i in range(len(years_list)):
        year = years_list[i]
        n_grades = stat_val[year][1] 
        stat_val[year][0] /= float(n_grades)
        
                
    
    print(stat_val)                     
    return stat_val        

#Efnan Gülkanat
grades= pd.read_csv('grade_sample.csv')
grades.sort_values("StudID", inplace=True)
grades['CourseCode'] = grades['CourseCode'].apply(str)+ grades['CourseNum'].apply(str)
result=grades.drop(grades.columns[[2,3]], axis=1)
vector=result.pivot_table(values='Grade', index='StudID', columns='CourseCode', aggfunc='first')

students=pd.read_csv('student_sample.csv')
students.sort_values("StudID", inplace=True)
