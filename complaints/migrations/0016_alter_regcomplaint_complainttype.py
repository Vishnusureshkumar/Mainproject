# Generated by Django 3.2.20 on 2023-08-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0015_alter_regcomplaint_complainttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regcomplaint',
            name='complainttype',
            field=models.CharField(choices=[('Electricity', 'Electricity'), ('Plumbing', 'Plumbing'), ('Construction', 'Construction'), ('others', 'others')], max_length=200, null=True),
        ),
    ]
