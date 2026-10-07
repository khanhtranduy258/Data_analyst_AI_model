import json 
import sqlite3
import pandas as pd
from pymongo import MongoClient
data_path = "D:/Code/project_code/Project/data/processed/master_dataset.csv"

sqlite_db_path = "D:/Code/project_code/Project/data/database/courses_database.db"

df = pd.read_csv(data_path)

connection = sqlite3.connect(sqlite_db_path)
#function clean duplicate in dataset
def clean_duplicate(selected_cols, col_name):
    duplicate_values = df[selected_cols].duplicated().sum()
    print(f"số lượng {col_name} bị trùng: {duplicate_values}")
    df_clean = df[selected_cols].drop_duplicates(subset=[col_name])
    return df_clean

#Courses table
course_cols = ['course_id', 'course_title', 'price', 'level', 'subject', 'source_platform']
df_coursse = clean_duplicate(course_cols, 'course_id')
#export dataframe df_course to course table in sqlite
df_coursse.to_sql("Courses", connection, index=False, if_exists='replace')

#enrollments table
enrollments_cols = ['enrollment_id', 'course_id', 'student_name', 'student_email', 'rating_score', 'completion_rate', 'enrollment_date', 'payment_method']
df_enrollments = clean_duplicate(enrollments_cols, 'enrollment_id') 
#handle enrollments with no course registraction
df_enrollments = df_enrollments.dropna(subset=['enrollment_id'])
#export dataframe df_enrollments to enrollments table in sqlite
df_enrollments.to_sql("Enrollments", connection, index=False, if_exists='replace')

#close connection 
connection.close()
print(f"đã lưu thành công vào sqlite tại: {sqlite_db_path}")

#query data
tables = ["Courses", "Enrollments"]
try:
    with sqlite3.connect(sqlite_db_path) as conn:
        cur = conn.cursor()
        for table in tables: 
            cur.execute("SELECT * FROM " + table)
            row = cur.fetchone()
            print(f"mẫu 1 hàng dữ liệu trong {table} là: ")
            print(row)
except sqlite3.Error as e:
    print(e)

