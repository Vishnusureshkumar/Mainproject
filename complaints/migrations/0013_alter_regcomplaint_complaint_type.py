# Generated by Django 3.2.20 on 2023-08-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0012_alter_regcomplaint_complaint_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regcomplaint',
            name='complaint_type',
            field=models.CharField(choices=[('Elecricity', 'Elecricity'), ('Plumbing & Drainage', 'Plumbing & Drainage'), ('Construction', 'Construction')], max_length=200, null=True),
        ),
    ]
