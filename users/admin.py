from django.contrib import admin

from users.models import Address, Donor, User

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Address)
