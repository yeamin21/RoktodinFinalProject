# Generated by Django 3.2.6 on 2021-11-24 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_donor_share_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='postal',
            new_name='are_zip',
        ),
    ]