import os
import requests
import pandas as pd
import requests
import os

df = pd.read_csv("vanban.csv")

os.makedirs("pdfs", exist_ok=True)

for _, row in df[df['Bản PDF'].notna()].iterrows():
    url = row['Bản PDF']
    name = row['Tên văn bản'].replace("/", "_").replace("\\", "_")[:50] + ".pdf"
    try:
        res = requests.get(url, timeout=10)
        if res.ok:
            with open(f"pdfs/{name}", "wb") as f:
                f.write(res.content)
            print("✅ Tải:", name)
        else:
            print("❌ Không tải được:", url)
    except Exception as e:
        print("⚠️ Lỗi:", e)

# Tạo thư mục lưu PDF nếu chưa có
pdf_dir = "vanban_pdfs"
os.makedirs(pdf_dir, exist_ok=True)

# Chỉ lấy các dòng có link PDF hợp lệ
pdf_links = df[df['Bản PDF'].notna()][['Tên văn bản', 'Bản PDF']]

# Danh sách tên file đã tải
downloaded_files = []

# Tải từng file PDF
for _, row in pdf_links.iterrows():
    name = row['Tên văn bản'].replace("/", "_").replace("\\", "_")[:50]
    url = row['Bản PDF']
    try:
        response = requests.get(url, timeout=10)
        if response.ok:
            filename = f"{name}.pdf"
            filepath = os.path.join(pdf_dir, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            downloaded_files.append(filename)
    except Exception as e:
        print(f"Lỗi khi tải {url}: {e}")

downloaded_files
