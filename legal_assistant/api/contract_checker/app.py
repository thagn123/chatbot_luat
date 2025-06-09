from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_file_to_telegram(filepath, filename):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
    with open(filepath, "rb") as f:
        files = {"document": (filename, f)}
        data = {"chat_id": CHAT_ID}
        response = requests.post(url, data=data, files=files)
        return response.json()

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/api/check_contract', methods=['POST'])
def check_contract():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    tg_result = send_file_to_telegram(filepath, file.filename)

    if tg_result.get("ok"):
        message = "✅ File đã được gửi tới Telegram để kiểm tra."
    else:
        message = "❌ Gửi file đến Telegram thất bại."

    return jsonify({'result': message})
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/check_contract', methods=['POST'])
def check_contract():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Giả lập xử lý – phân tích đơn giản nội dung
    content = file.read().decode('utf-8')

    # Xử lý logic – ở đây là ví dụ tĩnh
    report = """
### Tóm tắt điều khoản

#### Điều khoản 1
Nội dung điều khoản 1  
**Bên A**: CÔNG TY A  
**Bên B**: CÔNG TY B  
**Rủi ro**: Không rõ trách nhiệm thanh toán  
**Đề xuất**: Làm rõ thời hạn và phương thức thanh toán

#### Điều khoản 2
Nội dung điều khoản 2  
**Bên A**: CÔNG TY A  
**Bên B**: CÔNG TY B  
**Rủi ro**: Không quy định chế tài vi phạm  
**Đề xuất**: Thêm điều khoản xử lý vi phạm

_(Báo cáo sinh tự động)_
    """

    return jsonify({'report': report})

if __name__ == '__main__':
    app.run(debug=True)
