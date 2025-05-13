from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm  # Tạo form đăng ký tùy chỉnh
from django.http import HttpResponse
from documents.models import LegalDocument
from subscription.models import Subscription

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập tự động sau khi đăng ký
            return redirect("/users/dashboard/")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def index(request):
    return HttpResponse("Chào mừng bạn đến với trang người dùng của ứng dụng Pháp Luật!")


def user_dashboard(request):
    user = request.user
    documents = LegalDocument.objects.all()[:5]  # Hiển thị 5 tài liệu mới
    subscriptions = Subscription.objects.filter(user=user)

    context = {
        'user': user,
        'documents': documents,
        'subscriptions': subscriptions,
    }
    return render(request, 'users/dashboard.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/users/login/')  # Điều hướng về trang đăng nhập sau khi đăng xuất
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/users/dashboard/")
        else:
            return render(request, "users/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
    return render(request, "users/login.html")
def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

