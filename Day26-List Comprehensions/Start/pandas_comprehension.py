import pandas as pd

student={"student":["Angela","James","Lily"],
         "scores":[56,76,98]}

student_data=pd.DataFrame(student)

#looping through rows of the datafrome

for (index,row) in student_data.iterrows():
    print(index)
    print(row)