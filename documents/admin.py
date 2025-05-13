from django.contrib import admin
from .models import LegalDocument

class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'law_type', 'crawl_time', 'effective_start', 'effective_end', 'tag')
    list_filter = ('law_type', 'tag')
    search_fields = ('title',)

admin.site.register(LegalDocument, LegalDocumentAdmin)