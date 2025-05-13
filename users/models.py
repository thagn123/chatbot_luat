from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('nhanvien', 'Nhân viên pháp chế'),
        ('vanphong', 'Văn phòng công chứng'),
        ('nguoidung', 'Người dùng không có chuyên môn về Luật'),
        ('congan', 'Công An'),
        ('toaan', 'Viện kiểm soát Tòa Án'),
        ('moigioi', 'Môi giới BDS'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='nguoidung')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"