# Generated by Django 3.2.20 on 2023-08-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0018_rename_contact_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='regcomplaint',
            name='status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('InProgress', 'InProgress'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
    ]
