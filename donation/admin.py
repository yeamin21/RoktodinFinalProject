from donation.models import BloodRequest, BloodRequestResponse, Hospital, PhoneShareRequest
from django.contrib import admin

admin.site.register(BloodRequest)
admin.site.register(Hospital)
admin.site.register(PhoneShareRequest)
admin.site.register(BloodRequestResponse)