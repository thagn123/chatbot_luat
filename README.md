# chatbot_luat
## 📦 Các thư viện cần thiết
Đặt Chỉ ở legal_assistant/legal_assistant
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
```
### Chạy file ""crawl_vanban.py"" - Để lấy link tải các văn bản pháp luật mới nhất
tiếp tục chạy file " hhh.py" - Tải các văn bản PDF 
----Các văn bản sẽ được lưu trong thư mục "pdfs"
