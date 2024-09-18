from django.urls import path
from django.views.generic import TemplateView
from .views import upload_file

app_name = "myapp"

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('upload/success/', TemplateView.as_view(template_name='success.html'), name='upload_success'),
]
