from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import enum


class User(AbstractUser):
    pass


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=2, choices=[('a+', 'a+'), ('b+', 'b+')])
    phone = PhoneNumberField(blank=False, null=False)
    share_phone = models.BooleanField(default=True)


class RequestPhoneOrEmail(models.Model):
    requesting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_user')
    message_body = models.CharField(max_length=70)
