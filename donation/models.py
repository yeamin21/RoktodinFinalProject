from django.db import models
from users.models import User


class BloodRequest(models.Model):
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_receiver')
    no_bag_required = models.IntegerField()
    no_bag_managed = models.IntegerField()
    is_emergency = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.receiver} requested {self.no_bag_required}'
