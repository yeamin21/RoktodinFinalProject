# Generated by Django 3.2.6 on 2021-12-02 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20211128_2230'),
        ('donation', '0009_bloodrequestresponse'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bloodrequestresponse',
            unique_together={('blood_request', 'respondent')},
        ),
    ]
