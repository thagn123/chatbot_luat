from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
@api_view(['POST'])


def ask_chatbot(request):
    import json
    from django.views.decorators.csrf import csrf_exempt

    @csrf_exempt
    def inner(request):
        data = json.loads(request.body)
        question = data.get('question', '')
        # Dummy response
        answer = "Đây là câu trả lời cho: " + question
        return JsonResponse({'answer': answer})

    return inner(request)

from django.shortcuts import render

def copilot_interface(request):
    return render(request, 'copilot.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def documents_page(request):
    return render(request, 'documents.html')

def users_page(request):
    return render(request, 'users.html')

def feedback_page(request):
    return render(request, 'feedback.html')

def subscriptions_page(request):
    return render(request, 'subscriptions.html')
