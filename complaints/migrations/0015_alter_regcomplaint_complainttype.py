# Generated by Django 3.2.20 on 2023-08-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0014_rename_complaint_type_regcomplaint_complainttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regcomplaint',
            name='complainttype',
            field=models.CharField(choices=[('Electricity', 'Electricity'), ('Plumbing & Drainage', 'Plumbing & Drainage'), ('Construction', 'Construction"')], max_length=200, null=True),
        ),
    ]
