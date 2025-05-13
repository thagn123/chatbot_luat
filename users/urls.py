# users/urls.py
from django.urls import path
from . import views
from .views import user_dashboard, profile_view, logout_view, login_view, signup_view



urlpatterns = [
    # Thêm các URL endpoints của app users ở đây.
    # Ví dụ: nếu bạn có view xử lý trang chủ của người dùng, bạn có thể làm như sau:
    path('', views.index, name='users_index'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/', profile_view, name='user_profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Đã import đúng view
    path('signup/', signup_view, name='signup'),


    # Nếu chưa có view nào, bạn có thể để trống (nhưng cần khai báo urlpatterns):
]


