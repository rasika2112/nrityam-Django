# Generated by Django 3.0.3 on 2020-07-05 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200702_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNo', models.CharField(max_length=12)),
                ('feedback', models.TextField()),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
