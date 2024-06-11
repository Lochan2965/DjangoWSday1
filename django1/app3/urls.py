from django.urls import path
from .views import bank, created

urlpatterns = [
    path('', bank, name='bank'),
    path('created/<int:accno>/', created, name='created'),
]
