# qrscanner/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate_qr/', views.generate_qr_code, name='generate_qr_code'),  # URL to generate the QR code
    path('display_qr/', views.display_qr_code, name='display_qr_code'),  # URL to display the QR code
]
