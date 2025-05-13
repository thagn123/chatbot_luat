from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chatbot/', include('chatbot.urls')),
    # Bạn có thể thêm các endpoint khác:
    path('api/users/', include('users.urls')),
    path('api/documents/', include('documents.urls')),
    path('api/subscriptions/', include('subscription.urls')),
    path('api/telegram/', include('telegram_bot.urls')),


    # Thêm các endpoint API khác nếu cần:
    # path('api/users/', include('users.urls')),
    # path('api/documents/', include('documents.urls')),
    # path('api/subscriptions/', include('subscription.urls')),
    # Ngoài ra, bạn cũng có thể khai báo view cho giao diện người dùng:
    path('chat/', include('chatbot.urls')),  # hoặc cấu hình riêng cho giao diện web
]
