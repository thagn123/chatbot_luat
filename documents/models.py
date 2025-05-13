from django.db import models


class LegalDocument(models.Model):
    LAW_TYPE_CHOICES = [
        ('bo_luat', 'Bộ luật'),
        ('luat', 'Luật'),
        ('nghi_dinh', 'Nghị định'),
        ('nghi_quyet', 'Nghị quyết'),
    ]

    TAG_CHOICES = [
        ('chinh_tri', 'Chính trị'),
        ('dat_dai', 'Đất đai'),
        ('kinh_te', 'Kinh tế'),
    ]

    title = models.CharField(max_length=255)
    law_type = models.CharField(max_length=20, choices=LAW_TYPE_CHOICES)
    crawl_time = models.DateTimeField(auto_now_add=True, help_text="Thời gian crawl dữ liệu")
    effective_start = models.DateField(help_text="Ngày bắt đầu có hiệu lực")
    effective_end = models.DateField(null=True, blank=True, help_text="Ngày hết hiệu lực, nếu có")
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.get_law_type_display()}"