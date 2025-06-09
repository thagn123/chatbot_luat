from django.urls import path
from .views import ask_chatbot


from .views import ask_chatbot, copilot_interface

urlpatterns = [
    path('ask/', ask_chatbot, name='ask_chatbot'),
    path('copilot/', copilot_interface, name='copilot_ui'),
]