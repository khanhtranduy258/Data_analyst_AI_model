#Dataset 1 (Udemy course): https://www.kaggle.com/datasets/andrewmvd/udemy-courses
#Dataset 2 (Online course): https://www.kaggle.com/datasets/khaledatef1/online-courses

import pandas as pd
#read file
df_udemy_course = pd.read_csv("D:/Code/project_code/Project/data/raw/udemy_courses.csv")
df_online_course = pd.read_csv("D:/Code/project_code/Project/data/raw/Online_Courses.csv")
df_user_enrollment = pd.read_csv("D:/Code/project_code/Project/data/raw/user_enrollments.csv")

def show_info_dataset(dataset_name, df):
    print("tên dataset:", dataset_name)
    print(f"số dòng: {df.shape[0]}")
    print(f"số cột: {df.shape[1]}")
    print("tên cột: ")
    print(df.columns.tolist())
    print("5 dòng đầu tiên của dataset: ")
    print(df.head())
    print("-"*50)

# show information udemy courses dataset
show_info_dataset("udemy courses", df_udemy_course)
#show information online courses dataset
show_info_dataset("online courses", df_online_course)
#show information user enrollment dataset
show_info_dataset("user enrollment", df_user_enrollment)

