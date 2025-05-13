import os
import requests

# Lấy token của Bot từ biến môi trường hoặc thay thế trực tiếp bằng token của bạn
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '8156420234:AAGSO0CtOXet4gRnMjbjPqlweWa6jSBlLbQ')
# Thiết lập URL webhook (chú ý: URL phải là HTTPS và có thể truy cập từ Internet)
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'https://your-domain.com/api/telegram/webhook/')

# Đường dẫn API của Telegram để set webhook
set_webhook_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"

payload = {
    'url': WEBHOOK_URL,
}

response = requests.post(set_webhook_url, data=payload)

if response.status_code == 200:
    print("Webhook đã được thiết lập thành công!")
else:
    print("Thiết lập webhook thất bại. Chi tiết:", response.text)