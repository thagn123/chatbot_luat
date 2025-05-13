from django.shortcuts import render
from .models import Subscription

def subscription_dashboard(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscription/dashboard.html', {'subscriptions': subscriptions})