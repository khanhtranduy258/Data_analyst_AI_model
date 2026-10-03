import pandas as pd
from faker import Faker

fake = Faker()
#get file path for two dataset: udemy course and online course
FILE_PATH_UDEMY = "D:/Code/project_code/Project/data/raw/udemy_courses.csv"
FILE_PATH_ONLINE = "D:/Code/project_code/Project/data/raw/Online_Courses.csv"
#read dataset
df_udemy = pd.read_csv(FILE_PATH_UDEMY)
df_online = pd.read_csv(FILE_PATH_ONLINE)
#choose the common columns in each dataset 
common_udemy_cols = ["course_id", "course_title", "price", "level", "subject"]
common_online_cols = ["Course Title", "Price", "Level", "Category"]
#create sub dataset from original dataset
#udemy courses
df_udemy_sub = df_udemy[common_udemy_cols].copy()
df_udemy_sub['course_id'] = df_udemy_sub['course_id'].astype(str)
df_udemy_sub["source_platform"] = "Udemy Courses"
#online courses
df_online_sub = df_online[common_online_cols].copy()
df_online_sub = df_online_sub.rename(columns={
    "Course Title": "course_title",
    "Price": "price",
    "Level":"level",
    "Category":"subject"
})
#generate course_id for online courses dataset
concat_id = "ONLINE"
course_online_ids = []
for i in range(len(df_online_sub)):
    item = (concat_id + str(fake.unique.random_int(min=111111, max=999999)))
    course_online_ids.append(item)

df_online_sub["course_id"] = course_online_ids
df_online_sub['source_platform'] = "Online Courses"
#show sub dataset
print("Udemy Courses: ")
print(df_udemy_sub)
print("-"*50)
print("Online Courses: ")
print(df_online_sub)
#concat dataset
unified_courses = pd.concat([df_udemy_sub, df_online_sub], ignore_index=True)
#show unified courses after concating
print("-"*50)
print("dataset sau khi concat là: ")
print(unified_courses)
#merge dataset between the result of concat above and dynamic data generated from step 2
FILE_PATH_ENROLLMENT = "D:/Code/project_code/Project/data/raw/user_enrollments.csv"
df_enrollment = pd.read_csv(FILE_PATH_ENROLLMENT)
#chage course_id columns in df_enrollment from int to string
df_enrollment["course_id"] = df_enrollment["course_id"].astype(str)
master_dataset = pd.merge(unified_courses, df_enrollment, on="course_id", how='left')
print("master dataset sau khi merge là: ")
print(master_dataset.columns.tolist())
print(master_dataset)
#get 5 course_id in user_enrollments 
sample_course_ids = df_enrollment["course_id"].head(5)
result  = master_dataset[
    master_dataset["course_id"].isin(sample_course_ids)
]
print('-'*50)
print(result.columns.tolist())
print(result)
#export master_dataset to csv and save to data/processed
OUTPUT_processed = "D:/Code/project_code/Project/data/processed/master_dataset.csv"
master_dataset.to_csv(OUTPUT_processed, index=False)
