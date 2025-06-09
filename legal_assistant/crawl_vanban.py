import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Nhập từ khóa tìm kiếm từ người dùng (ví dụ: "Hiến Pháp")
keywords = input("Nhập các từ khóa cách nhau bởi dấu phẩy: ").split(",")

# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)  # Tăng timeout nếu cần

# Truy cập trang tìm kiếm VBPL
driver.get("https://vbpl.vn/TW/Pages/vbpq-timkiem.aspx?dvid=13")

# Danh sách dữ liệu để lưu (mỗi phần tử là một từ điển chứa thông tin văn bản)
documents = []

for keyword in keywords:
    keyword = keyword.strip()
    print(f"Tìm kiếm: {keyword}")

    # Chờ ô tìm kiếm xuất hiện và nhập từ khóa
    search_box = wait.until(EC.presence_of_element_located((By.ID, "AdvanceKeyword")))
    search_box.clear()
    search_box.send_keys(keyword)

    # Click nút tìm kiếm
    search_button = driver.find_element(By.ID, "searchSubmit")
    search_button.click()

    # Chờ kết quả hiển thị; nếu trang có ajax, chúng ta đợi đến khi khối kết quả có ID "grid_vanban" xuất hiện
    wait.until(EC.presence_of_element_located((By.ID, "grid_vanban")))
    time.sleep(2)  # Chờ thêm nếu cần

    # Lấy HTML kết quả từ phần chứa kết quả: "grid_vanban"
    html = driver.find_element(By.ID, "grid_vanban").get_attribute("innerHTML")
    soup = BeautifulSoup(html, "html.parser")

    # Lấy số kết quả tìm được (nếu có trong tiêu đề của khối kết quả)
    header_div = soup.find("div", class_="header")
    total_results = ""
    if header_div:
        total_results = header_div.get_text(strip=True)

    # Lấy thông tin từng văn bản
    # Giả sử mỗi văn bản được hiển thị trong một thẻ <div class="item"> (hoặc phần tử tương tự, chỉnh sửa nếu cần)
    results = soup.find_all("div", class_="item")[:5]  # Lấy 5 kết quả đầu tiên

    for result in results:
        try:
            # Tên văn bản và URL toàn văn
            a_tag = result.find("a")
            if a_tag is None:
                continue
            title = a_tag.get_text(strip=True)
            full_text_url = "https://vbpl.vn" + a_tag["href"]

            # Tìm các liên kết phụ dựa vào nhãn của chúng.
            # Mẫu mẫu dữ liệu bạn đưa ra:
            # Bản PDF: đường dẫn từ <li class="source"><a ...>
            # VB liên quan: từ <li class="ref"><a ...>
            # Thuộc tính: từ <li class="thuoctinh"><a ...>
            # Lược đồ: từ <li class="map"><a ...>
            # Tải về: từ <li class="download"><a ...>
            pdf_link = ""
            ref_link = ""
            attributes_link = ""
            map_link = ""
            download_link = ""

            for li in result.find_all("li"):
                # Lấy văn bản trong thẻ <a> và dựa vào class hoặc nhãn bên ngoài
                a = li.find("a")
                if a and a.get_text(strip=True):
                    text = a.get_text(strip=True).lower()
                    href = a.get("href", "")
                    if "pdf" in li.get("class", []) or "source" in li.get("class", []):
                        pdf_link = "https://vbpl.vn" + href if href.startswith("/") else href
                    elif "ref" in li.get("class", []):
                        ref_link = "https://vbpl.vn" + href if href.startswith("/") else href
                    elif "thuoctinh" in li.get("class", []):
                        attributes_link = "https://vbpl.vn" + href if href.startswith("/") else href
                    elif "map" in li.get("class", []):
                        map_link = "https://vbpl.vn" + href if href.startswith("/") else href
                    elif "download" in li.get("class", []):
                        download_link = href  # Đây thường là một lời gọi JS (ví dụ: "javascript:ShowDialogDownload(32801);")
            # Tạo từ điển cho văn bản
            doc = {
                "Tổng kết quả": total_results,
                "Tên văn bản": title,
                "Toàn văn": full_text_url,
                "Bản PDF": pdf_link,
                "VB liên quan": ref_link,
                "Thuộc tính": attributes_link,
                "Lược đồ": map_link,
                "Tải về": download_link
            }
            documents.append(doc)
        except Exception as e:
            print(f"Lỗi xử lý văn bản: {e}")
            continue

# Ghi danh sách tài liệu vào tệp CSV nếu có dữ liệu thu thập được
if documents:
    filename = "vanban.csv"
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=documents[0].keys())
        writer.writeheader()
        writer.writerows(documents)
    print(f"✅ Đã lưu thông tin văn bản vào tệp '{filename}'.")
else:
    print("❌ Không tìm thấy dữ liệu văn bản hợp lệ.")

driver.quit()