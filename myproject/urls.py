from django.contrib import admin
from django.urls import path
from certificates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('certificate/<int:certificate_id>/', views.certificate_details, name='certificate_details'),
    path('certificate/<int:certificate_id>/download/<str:file_type>/', views.download_certificate, name='download_certificate'),]