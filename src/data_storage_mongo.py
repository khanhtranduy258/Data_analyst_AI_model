import json
import pandas as pd
from pymongo import MongoClient

data_path = "D:/Code/project_code/Project/data/processed/master_dataset.csv"
df = pd.read_csv(data_path)

def clean_duplicate(selected_cols, col_name):
    duplicate_values = df[selected_cols].duplicated().sum()
    print(f"số lượng {col_name} bị trùng: {duplicate_values}")
    df_clean = df[selected_cols].drop_duplicates(subset=[col_name])
    return df_clean

course_cols = ['course_id', 'course_title', 'price', 'level', 'subject', 'source_platform']
df_course = clean_duplicate(course_cols, 'course_id')

enrollments_cols = ['enrollment_id', 'course_id', 'student_name', 'student_email', 'rating_score', 'completion_rate', 'enrollment_date', 'payment_method']
df_enrollments = clean_duplicate(enrollments_cols, 'enrollment_id') 
df_enrollments = df_enrollments.dropna(subset=['enrollment_id'])

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["course_management_db"]
    collection = db['Courses']

    #clean old collection
    collection.delete_many({})
    
    mongo_docs = []

    for _, course in df_course.iterrows():
        c_id = course['course_id']
        matching_enrollments = df_enrollments[df_enrollments['course_id'] == c_id]
        matching_enrollments.columns = matching_enrollments.columns.astype(str)
        enrollments = matching_enrollments.to_dict(orient="records")

        doc = {
            "course_id": str(c_id),
            "course_title": course["course_title"],
            "price": float(course["price"]) if pd.notna(course["price"]) else 0.0,
            "level": course["level"],
            "subject": course["subject"],
            "source_platform": course["source_platform"],
            "enrollments": enrollments  
        }
        mongo_docs.append(doc)

    if mongo_docs:
        collection.insert_many(mongo_docs)
        print(f" Đã nạp thành công {len(mongo_docs)} Documents vào MongoDB!")
except Exception as e:
    print("lỗi kết nối mongodb: ", e)
