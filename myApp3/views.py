from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicalRecordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class PatientMedicalRecordsAPIView(APIView):
    def get(self, request, pk):
        records = MedicalRecord.objects.filter(patient_id=pk)
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data)
