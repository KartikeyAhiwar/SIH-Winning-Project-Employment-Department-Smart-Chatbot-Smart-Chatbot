# Generated by Django 5.0 on 2023-12-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_registeration_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
