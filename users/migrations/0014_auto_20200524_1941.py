# Generated by Django 3.0.6 on 2020-05-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200524_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('bombay', 'Bombay')], max_length=15, null=True),
        ),
    ]
