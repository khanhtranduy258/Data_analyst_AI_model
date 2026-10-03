import random 
from faker import Faker 
import numpy as np
import pandas as pd

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# 2. Lấy danh sách course_id thực tế từ dataset Udemy của bạn
# (Giúp việc Merge ở Bước 3 khớp 100% khóa chính - khóa ngoại)
df_udemy = pd.read_csv(
    "D:/Code/Python/Project/data/raw/udemy_courses.csv"
)
existing_course_ids = df_udemy["course_id"].tolist()

# 3. Sinh 1,500 bản ghi giao dịch/học viên giả lập
num_records = 1500
dynamic_data = []

for i in range(1, num_records + 1):
    record = {
        "enrollment_id": f"ENROLL_{i:05d}",  # Mã đăng ký (Khóa chính bảng động)
        "student_name": fake.name(),  # Tên học viên
        "student_email": fake.email(),  # Email học viên
        "course_id": random.choice(
            existing_course_ids
        ),  # Mã khóa học (Khóa ngoại kết nối với Udemy)
        "rating_score": round(
            random.uniform(1.0, 5.0), 1
        ),  # Điểm đánh giá (1.0 - 5.0)
        "completion_rate": random.randint(
            10, 100
        ),  # Tiến độ học (%)
        "enrollment_date": fake.date_between(
            start_date="-2y", end_date="today"
        ),  # Ngày đăng ký
        "payment_method": random.choice(
            ["Credit Card", "PayPal", "Bank Transfer"]
        ),
    }
    dynamic_data.append(record)

# 4. Chuyển thành DataFrame
df_dynamic = pd.DataFrame(dynamic_data)

# 5. Lưu ra file CSV tại thư mục data/raw/ (Dữ liệu thô giả lập)
output_path = "D:/Code/Python/Project/data/raw/dynamic_user_enrollments.csv"
df_dynamic.to_csv(output_path, index=False, encoding="utf-8-sig")

print("=" * 50)
print("ĐÃ TẠO THÀNH CÔNG DỮ LIỆU ĐỘNG (STEP 2)!")
print("Kích thước dữ liệu:", df_dynamic.shape)
print("File đã lưu tại:", output_path)
print("=" * 50)
print(df_dynamic.head())