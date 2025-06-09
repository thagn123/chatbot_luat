from django.db import models

class LegalDocument(models.Model):
    CATEGORY_CHOICES = [
        ('code', 'Bộ luật'),
        ('law', 'Luật'),
        ('decree', 'Nghị định'),
        ('resolution', 'Nghị quyết'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    issue_date = models.DateField()
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    tag = models.CharField(max_length=100)
    content = models.TextField()
    source_url = models.URLField()
    crawl_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title