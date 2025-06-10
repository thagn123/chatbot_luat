# chatbot_luat


## Yêu Cầu

- Python 3.x
- Các thư viện cần thiết (liệt kê bên dưới)

## Cài Đặt

1. **Clone Dự Án**:
 
## 📦 Các thư viện cần thiết
Đặt Chỉ ở legal_assistant
Dưới đây là danh sách các thư viện quan trọng để chạy dự án này:

###  **Web Scraping & Automation**
- `selenium` – Tự động hóa trình duyệt web.
- `BeautifulSoup` – Trích xuất dữ liệu từ HTML.
- `requests` – Gửi HTTP requests để lấy nội dung trang web.

###  **Xử lý Dữ liệu**
- `csv` – Đọc/ghi tệp CSV để lưu trữ dữ liệu.
- `os` – Quản lý tệp hệ thống và thư mục.

###  **Tạo file PDF**
- `reportlab` – Xuất và định dạng file PDF.

### **Chờ & Tương tác với Web**
- `time` – Tạo độ trễ giữa các thao tác Selenium.
- `webdriver` (từ Selenium) – Điều khiển trình duyệt.
- `By`, `WebDriverWait`, `expected_conditions` – Xử lý phần tử trên trang web.

## Cài đặt thư viện
cài đặt tất cả các thư viện trên bằng lệnh:
```
pip install -r requirements.txt
```
## Chạy thư Mục
Chạy web bằng dòng lệnh
```
python manage.py runserver
Chạy Telegram_bot
python telegram_bot/bot.py
TOKEN trong file .env
```
