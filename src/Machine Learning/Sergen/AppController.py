
## Sergen ISPIR

from Tables import *
import CourseGradeController as cgc

def main():
    
    ## data preparation
    c = [0,0.5,1,1.5,2,2.5,3,3.5,4]
    x = courseTable[:]
    course_name = 'ceng241'
    course_list = [i.lower() for i in courseList]
    class_index = course_list.index('ceng241')
    y = x[:,class_index] ## class label
    x = np.delete(x,class_index,1) ## remove class column from input data

    ## change y label with class value (eg. if y[0] = 3.5 then it become 7th class)
    for i in range(y.size):
            index = c.index(y[i])
            y[i] = index

    cgc.course_grade_logistic(x,y)
    cgc.course_grade_MLP(x,y)

if __name__ == "__main__":
    main()
