from faker import Faker
from random import randint
import pandas as pd
import random

fake = Faker()

#get course id from udemy courses dataset
FILE_PATH_UDEMY_COURSES = "D:/Code/project_code/Project/data/raw/udemy_courses.csv"
df_udemy = pd.read_csv(FILE_PATH_UDEMY_COURSES)
existing_course_ids = df_udemy["course_id"].tolist()

# number reconds transaction/student simulation
NUM_RECONDS = 1500
concat_id = "ID"
data = []
for index in range(NUM_RECONDS):
    recond = {
        "enrollment_id": (concat_id + str(fake.unique.random_int(min=111111, max=999999))),
        "student_name": fake.name(),
        "student_email": fake.email(),
        "course_id": random.choice(existing_course_ids),
        "rating_score": round(random.uniform(1.0, 5.0), 1),
        "completion_rate": random.randint(1, 100),
        "enrollment_date": fake.date(),
        "payment_method": random.choice(['Credit card', 'Paypal', 'Bank Transfer'])
    }
    data.append(recond)

#convert array to dataframe
data_df = pd.DataFrame(data)
#export csv file to the specific path raw folder
OUTPUT_PATH  = "D:/Code/project_code/Project/data/raw/user_enrollments.csv"
data_df.to_csv(OUTPUT_PATH, index=False)
#show result
print("đã tạo dynamic data thành công!")
print("thông tin tổng quan dynamic dataset đã tạo:")
print("path: ", OUTPUT_PATH)
print(f"số dòng: {data_df.shape[0]}")
print(f"số cột: {data_df.shape[1]}")
print("hiển thị 5 dòng đầu tiên của dataset:")
print(data_df.head())