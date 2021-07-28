from django.contrib import admin

from users.models import Donor, User

admin.site.register(User)
admin.site.register(Donor)
