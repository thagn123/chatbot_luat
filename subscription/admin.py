from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'start_date', 'expiry_date', 'status')
    list_filter = ('status', 'package')
    search_fields = ('user__username',)

admin.site.register(Subscription, SubscriptionAdmin)