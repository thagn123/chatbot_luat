from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('corporate_legal', 'Nhân viên pháp chế'),
        ('notary', 'Văn phòng công chứng'),
        ('layperson', 'Người dùng không chuyên'),
        ('police', 'Công an'),
        ('prosecutor_court', 'Viện KS/Toà án'),
        ('real_estate_agent', 'Môi giới BĐS'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)