# Generated by Django 3.1.7 on 2021-09-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_upcoming_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcoming_classes',
            name='link',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
