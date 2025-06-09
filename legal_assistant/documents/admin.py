from django.contrib import admin
from .models import LegalDocument

@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'issue_date', 'effective_from', 'effective_to', 'tag')
    search_fields = ('title', 'tag')