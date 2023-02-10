from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,patient_dashboard,doctor_dashboard,dashboard

app_name = 'InterWebApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("dashboard/", dashboard, name="dashboard"),
    path("patient_dashboard/", patient_dashboard, name="patient_dashboard"),
    path("doctor_dashboard/", doctor_dashboard, name="doctor_dashboard"),

  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



