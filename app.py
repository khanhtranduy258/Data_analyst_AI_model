import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Course Enrollment Prediction', page_icon='🎓', layout='centered'
)

# 2. Load mô hình đã lưu từ file .pkl (Đổi lại đường dẫn nếu bạn lưu trong thư mục 'models')
model_path = "D:/Code/project_code/Project/saved_models/course_classifier_model.pkl"

@st.cache_resource
def load_model():
  return joblib.load(model_path)


model = load_model()

# 3. Tiêu đề giao diện
st.title(' Dự Đoán Khả Năng Đăng Ký Khóa Học')
st.markdown(
    'Sử dụng mô hình **Decision Tree Classifier** để dự đoán xem khóa học có'
    ' đạt tỷ lệ đăng ký cao hay không dựa trên các thông số bên dưới.'
)
st.markdown('---')

# 4. Tạo các thành phần nhập liệu cho người dùng (Sliders / Number inputs)
st.subheader('Nhập thông tin khóa học:')

# Dựa vào các đặc trưng: price, rating_score, completion_rate
price = st.number_input(
    'Giá khóa học (USD hoặc VNĐ):', min_value=0.0, max_value=1000.0, value=50.0
)
rating_score = st.slider(
    'Điểm đánh giá trung bình (Rating Score):',
    min_value=1.0,
    max_value=5.0,
    value=4.2,
    step=0.1,
)
completion_rate = st.slider(
    'Tỷ lệ hoàn thành khóa học (%):',
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=0.5,
)

# 5. Nút bấm dự đoán
if st.button('Dự Đoán Ngay', type='primary'):
  # Đưa dữ liệu đầu vào vào DataFrame với đúng tên cột lúc train mô hình
  input_data = pd.DataFrame({
      'price': [price],
      'rating_score': [rating_score],
      'completion_rate': [completion_rate],
  })

  # Dự đoán kết quả
  prediction = model.predict(input_data)[0]
  prediction_proba = model.predict_proba(input_data)[
      0
  ]  # Lấy xác suất dự đoán

  st.markdown('---')
  st.subheader('Kết quả dự đoán:')

  if prediction == 1:
    st.success(
        '🎉 **Kết quả: Khóa học có khả năng cao đạt đăng ký (`has_enrollment` ='
        f' 1)!**\n- Xác suất thành công:'
        f' **{prediction_proba[1]*100:.2f}%**'
    )
  else:
    st.warning(
        '**Kết quả: Khóa học ít có khả năng đạt đăng ký (`has_enrollment` ='
        f' 0).**\n- Xác suất rủi ro: **{prediction_proba[0]*100:.2f}%**'
    )