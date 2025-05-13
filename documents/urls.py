# documents/urls.py

from django.urls import path
from . import views  # nếu bạn có view nào cần import, ví dụ views.index

urlpatterns = [
    # Nếu bạn tạo view cho trang chủ của documents, ví dụ:
    # path('', views.index, name='documents_index'),
]