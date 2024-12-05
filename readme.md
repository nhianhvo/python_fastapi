# Hướng dẫn cài đặt và tạo project FastAPI

## 1. Cài đặt công cụ và môi trường
### Cài đặt Homebrew
bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### Cài đặt Python
bash
brew install python

## 2. Tạo project
### Tạo và di chuyển vào thư mục project
bash
mkdir my_fastapi_project
cd my_fastapi_project

### Tạo và kích hoạt môi trường ảo
bash
Tạo môi trường ảo
python -m venv venv
Kích hoạt môi trường ảo
source venv/bin/activate

## 3. Cài đặt các thư viện cần thiết
bash
pip install fastapi
pip install "uvicorn[standard]"

## 4. Tạo file main.py
python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
return {"Hello": "World"}

## 5. Chạy ứng dụng
bash
Chạy trên cổng mặc định (8000)
uvicorn main:app --reload
Hoặc chạy trên cổng tùy chọn
uvicorn main:app --reload --port 8001

## 6. Quản lý dependencies
bash
Lưu danh sách các thư viện đã cài đặt
pip freeze > requirements.txt

## 7. Các lệnh hữu ích khác
bash
Kiểm tra tiến trình đang sử dụng cổng
lsof -i :8000
Dừng tiến trình theo PID
kill -9 <PID>
Tắt môi trường ảo khi hoàn thành
deactivate
Xóa môi trường ảo (nếu cần)
rm -rf venv

### Các bước bổ sung nên thêm:

1. Thêm file `.gitignore` (nếu sử dụng git):
bash
Tạo file .gitignore
echo "venv/pycache/
.pyc
.env" > .gitignore

2. Tạo file `requirements.txt` ngay từ đầu (nếu biết trước các thư viện cần dùng):
bash
echo "fastapi
uvicorn[standard]" > requirements.txt
pip install -r requirements.txt

3. Tạo cấu trúc thư mục chuẩn cho project lớn:
bash
my_fastapi_project/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── routers/
│ ├── models/
│ └── schemas/
├── tests/
├── venv/
├── .gitignore
└── requirements.txt

Mở python shell 
python

tắt python shell
exit()/Control + D



Authentication
Cài đặt thư viện cần thiết:
Cài đặt python-jose để tạo và xác minh JWT:
    pip install "python-jose[cryptography]"
- Cài đặt passlib để băm mật khẩu:
     pip install "passlib[bcrypt]"
2. Tạo mô hình dữ liệu:
Tạo file app/models.py để định nghĩa mô hình dữ liệu:
Tạo service cho authentication:
Tạo file app/services/auth_service.py:
encoded_jwt
4. Tạo router cho authentication:
Tạo file app/routers/auth.py:

5. Tích hợp router vào ứng dụng chính:
Trong app/main.py, thêm router cho authentication:

6. Chạy ứng dụng:
Chạy ứng dụng của bạn với lệnh:
reload
7. Truy cập Swagger UI:
Mở trình duyệt và truy cập http://localhost:8000/docs
Bạn sẽ thấy endpoint /token để thực hiện đăng nhập và nhận token.
Với cấu trúc này, bạn có thể mở rộng thêm các chức năng khác cho authentication như đăng ký, xác thực token, v.v.