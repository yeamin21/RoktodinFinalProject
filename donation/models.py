from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import Address, BloodGroup, Donor, TimeStampMixin, User


class Hospital(TimeStampMixin):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    area_zip = models.IntegerField()
    country = models.CharField(max_length=50)

class BloodRequest(TimeStampMixin):
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_receiver')
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.PROTECT)
    no_bag_required = models.IntegerField()
    no_bag_managed = models.IntegerField(null=True, blank=True)
    needs_on = models.DateTimeField(null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete= models.PROTECT)
    is_emergency = models.BooleanField(default=False)
    phone_additional = PhoneNumberField(blank=True,null=True)
    def __str__(self):
        return f'{self.receiver} requested {self.no_bag_required}'

class PhoneShareRequest(TimeStampMixin):
    receiver = models.ForeignKey(Donor, on_delete=models.PROTECT,related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.PROTECT,related_name='sender')
    has_read = models.BooleanField(default=False)
    has_shared = models.BooleanField(default=False)

class BloodRequestResponse(TimeStampMixin):
    blood_request = models.ForeignKey(BloodRequest, on_delete=models.PROTECT, related_name='blood_request')
    respondent = models.ForeignKey(Donor,on_delete=models.PROTECT, related_name='donor_profile')
    fullfilled =models.BooleanField(default=False)

    # class Meta:
    #     unique_together = [['blood_request', 'respondent']]