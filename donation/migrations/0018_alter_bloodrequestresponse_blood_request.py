# Generated by Django 4.0 on 2021-12-29 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0017_alter_bloodrequest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequestresponse',
            name='blood_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blood_requests', to='donation.bloodrequest'),
        ),
    ]
