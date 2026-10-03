import pandas as pd
df_udemy = pd.read_csv("D:/Code/Python/Project/data/raw/udemy_courses.csv")
df_online_course = pd.read_csv("D:/Code/Python/Project/data/raw/Online_Courses.csv")

print("udemy course: ")
print(df_udemy.shape)
print(df_udemy.columns.tolist())
print("-"*50)
print("online course: ")
print(df_online_course.shape)
print(df_online_course.columns.tolist())



