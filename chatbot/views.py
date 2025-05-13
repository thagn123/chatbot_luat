from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
class ChatbotAPIView(APIView):
    def post(self, request, format=None):
        user_query = request.data.get('query', '')
        answer = process_user_query(user_query)
        return Response({"answer": answer}, status=status.HTTP_200_OK)

def process_user_query(query):
    # Giả lập xử lý câu hỏi; ở đây bạn có thể tích hợp NLP hoặc truy vấn cơ sở dữ liệu
    return f"Kết quả của truy vấn: {query}"


def chatbot_view(request):
    context = {}
    if request.method == 'POST':
        user_query = request.POST.get('query')
        answer = process_user_query(user_query)
        context['answer'] = answer
        context['query'] = user_query
    return render(request, 'chatbot/chat_interface.html', context)