from django.urls import path
from . import views

app_name = 'goCart'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
]