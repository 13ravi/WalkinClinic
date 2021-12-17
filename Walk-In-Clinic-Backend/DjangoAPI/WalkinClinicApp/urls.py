from django.conf.urls import url
from WalkinClinicApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^patients/$',views.patientsApi),
    url(r'^patients/([0-9]+)$',views.patientsApi),

    url(r'^staff/$',views.staffApi),
    url(r'^staff/([0-9]+)$',views.staffApi),

    url(r'^appointments/$',views.appointmentsApi),
    url(r'^appointments/([0-9]+)$',views.appointmentsApi),

    url(r'^prescription/$',views.prescriptionApi),
    url(r'^prescription/([0-9]+)$',views.prescriptionApi),
    
    url(r'^SaveFile$', views.SaveFile),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
