import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            chat_id = data.get('message', {}).get('chat', {}).get('id')
            user_message = data.get('message', {}).get('text', '')

            # Xử lý thông điệp và tạo phản hồi
            response_text = f"Đây là phản hồi cho: {user_message}"

            # Ở đây bạn có thể tích hợp thêm logic gửi tin nhắn về Telegram nếu cần.
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "detail": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "detail": "Phương thức không hợp lệ"}, status=400)