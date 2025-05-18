from django.urls import path
from .views import (
    PatientListCreateAPIView,
    PatientRetrieveUpdateDestroyAPIView,
    MedicalRecordListCreateAPIView,
    MedicalRecordRetrieveUpdateDestroyAPIView,
    PatientMedicalRecordsAPIView
)

urlpatterns = [
    path('api/patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('api/patients/<int:pk>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-detail'),
    path('api/records/', MedicalRecordListCreateAPIView.as_view(), name='record-list-create'),
    path('api/records/<int:pk>/', MedicalRecordRetrieveUpdateDestroyAPIView.as_view(), name='record-detail'),
    path('api/patients/<int:pk>/records/', PatientMedicalRecordsAPIView.as_view(), name='patient-records'),
]
