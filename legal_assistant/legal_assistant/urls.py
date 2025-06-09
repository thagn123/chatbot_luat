from django.contrib import admin
from django.urls import path, include
from chatbot.views import copilot_interface, home, documents_page, users_page, feedback_page, subscriptions_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('documents/', include('documents.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('feedback/', include('feedback.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('api/', include('api.urls')),
    path('', home, name='home'),
    path('chatbot/copilot/', copilot_interface, name='copilot_ui'),
    path('documents/', documents_page, name='documents'),
    path('users/', users_page, name='users'),
    path('feedback/', feedback_page, name='feedback'),
    path('telegram/', include('telegram_bot.urls')),
    path('subscriptions/', subscriptions_page, name='subscriptions'),

]