# Generated by Django 3.2.6 on 2021-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20211124_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodgroup',
            name='type',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('ab', 'AB'), ('o', 'O')], max_length=2),
        ),
    ]