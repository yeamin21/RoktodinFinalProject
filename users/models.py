from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import enum

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        abstract = True
class User(AbstractUser):
    pass

class BloodGroup(TimeStampMixin):
    type = models.CharField(
        max_length=2,
        choices=[('a', 'A'),
                 ('b', 'B'),
                 ('ab', 'AB'),
                 ('o', 'O')],null=False,blank=False)
    factor = models.CharField(max_length=1, choices=[('p','+'),('n','-')],null=False,blank=False)
    class Meta:
        unique_together = [['type', 'factor']]
    def __str__(self) -> str:
        return f'{self.type}{self.get_factor_display()}'
class Donor(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_details')
    is_donor = models.BooleanField(default=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.PROTECT)
    phone = PhoneNumberField(blank=False, null=False)
    share_phone = models.BooleanField(default=False)
    last_donation = models.DateField(null=True,blank=True)

class RequestPhoneOrEmail(models.Model):
    requesting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_user')
    message_body = models.CharField(max_length=70)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address')
    address = models.CharField(max_length=60) 
    postcode = models.IntegerField(max_length=6)
    city = models.CharField(max_length=40)
    district = models.CharField(max_length=40,blank=True, null=True)
    country = models.CharField(max_length=40,default='Bangladesh')


