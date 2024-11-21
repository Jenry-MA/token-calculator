from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate-tokens',views.calculate_tokens, name='calculate-tokens')
]