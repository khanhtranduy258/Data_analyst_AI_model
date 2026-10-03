#Dataset 1 (Udemy course): https://www.kaggle.com/datasets/andrewmvd/udemy-courses
#Dataset 2 (Online course): https://www.kaggle.com/datasets/khaledatef1/online-courses

import pandas as pd
#read file
df_udemy_course = pd.read_csv("D:/Code/project_code/Project/data/raw/udemy_courses.csv")
df_online_course = pd.read_csv("D:/Code/project_code/Project/data/raw/Online_Courses.csv")
# show information udemy courses dataset
print("Udemy courses dataset: ")
print("_"*50)
print("Shape: ", df_udemy_course.shape)
print("_"*50)
print("Columns name: ")
print(df_udemy_course.columns.tolist())
print("_"*50)
print("Data: ")
print(df_udemy_course)
print("="*50)
#show information online courses dataset
print("Online courses dataset: ")
print("_"*50)
print("Shape: ", df_online_course.shape)
print("_"*50)
print("Columns name: ")
print(df_online_course.columns.tolist())
print("_"*50)
print("Data:")
print(df_online_course)
