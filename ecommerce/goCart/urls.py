from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'goCart'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )