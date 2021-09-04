from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import enum


class User(AbstractUser):
    pass


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_details')
    blood_group = models.CharField(
        max_length=3,
        choices=[('a+', 'a+'),
                 ('b+', 'b+'),
                 ('a-', 'a-'),
                 ('b-', 'b-'),
                 ('ab+', 'ab+'),
                 ('ab-', 'ab-'),
                 ('o+', 'o+'),
                 ('o-', 'o-')])
    phone = PhoneNumberField(blank=False, null=False)
    share_phone = models.BooleanField(default=True)


class RequestPhoneOrEmail(models.Model):
    requesting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_user')
    message_body = models.CharField(max_length=70)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address')
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60, null=True, blank=True)
    postal = models.IntegerField(max_length=6)
    city = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    division = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
