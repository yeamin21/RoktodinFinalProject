from django.db import models
from django.db.models import fields
from rest_framework import serializers
from donation.models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
