from dataclasses import field
from rest_framework import serializers
from doctor.models import Doctor, Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    specialty = serializers.StringRelatedField(many=False)
    class Meta:
        model = Doctor
        fields = (
            'id',
            'name',
            'crm',
            'email',
            'specialty'
        )