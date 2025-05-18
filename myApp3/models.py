from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  


class MedicalRecord(models.Model):
    id = models.AutoField(primary_key=True) 
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='medical_records')  
    visit_date = models.DateField() 
    diagnosis = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} on {self.visit_date}" 