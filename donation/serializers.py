from django.db import models
from django.db.models import fields
from rest_framework import serializers
from donation.models import BloodRequest, BloodRequestResponse, PhoneShareRequest


class BloodRequestSerializer(serializers.ModelSerializer):

    receiver_full_name = serializers.SerializerMethodField(read_only=True)
    blood_group_name = serializers.SerializerMethodField(read_only=True)
    hospital_name = serializers.ReadOnlyField(source='hospital.name', read_only=True)
    hospital_city = serializers.ReadOnlyField(source='hospital.city', read_only=True)
    class Meta:
        model = BloodRequest
        fields = '__all__'
        extra_kwargs = {"needs_on": {"required": False, "allow_null": True}}
    def get_receiver_full_name(self,obj):
        return f'{obj.receiver.first_name} {obj.receiver.last_name}'
    def get_blood_group_name(self,obj):
        return f'{obj.blood_group.get_type_display()}{obj.blood_group.get_factor_display()}'


    def to_representation(self, instance):
        return super().to_representation(instance)

class PhoneShareRequestSerializer(serializers.ModelSerializer):
    sender_first_name = serializers.SerializerMethodField(read_only=True) 
    sender_last_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PhoneShareRequest
        fields = '__all__'
    def get_sender_first_name(self,obj):
        return obj.sender.first_name
    def get_sender_last_name(self,obj):
        return obj.sender.last_name

class BloodRequestResponseSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='respondent.user.first_name')
    last_name = serializers.ReadOnlyField(source='respondent.user.last_name')
    phone = serializers.ReadOnlyField(source='respondent.phone.as_national')
    hospital_name = serializers.ReadOnlyField(source='blood_request.hospital.name', read_only=True)
    hospital_city = serializers.ReadOnlyField(source='blood_request.hospital.city', read_only=True)
    bag_managed = serializers.ReadOnlyField(source='blood_request.no_bag_managed', read_only=True)
    bag_required = serializers.ReadOnlyField(source='blood_request.no_bag_required', read_only=True)
    phone_additional = serializers.ReadOnlyField(source='blood_request.phone_additional.as_national', read_only=True)
    is_emergency= serializers.ReadOnlyField(source='blood_request.is_emergency', read_only=True)
    request_created_at = serializers.ReadOnlyField(source='blood_request.created_at', read_only=True)
    needs_on= serializers.ReadOnlyField(source='blood_request.needs_on', read_only=True)
    class Meta:
        model =BloodRequestResponse
        fields ='__all__'
       