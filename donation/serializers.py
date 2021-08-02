from django.db import models
from django.db.models import fields
from rest_framework import serializers
from donation.models import BloodRequest


class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)
