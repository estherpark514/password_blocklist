# Generated by Django 5.1.3 on 2024-11-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_groups_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='raw_password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
