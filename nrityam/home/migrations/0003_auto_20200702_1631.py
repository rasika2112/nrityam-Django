# Generated by Django 3.0.3 on 2020-07-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200517_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.TextField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Course', models.CharField(max_length=100)),
                ('Rate', models.CharField(max_length=100)),
                ('Need', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cinfo',
        ),
        migrations.DeleteModel(
            name='Vinfo',
        ),
    ]
