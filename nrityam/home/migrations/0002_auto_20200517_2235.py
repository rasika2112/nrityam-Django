# Generated by Django 3.0.3 on 2020-05-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Aadhar', models.CharField(max_length=255)),
                ('Code', models.IntegerField()),
                ('PhoneNo', models.IntegerField()),
                ('Address', models.CharField(max_length=1000)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Vinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Aadhar', models.CharField(max_length=255)),
                ('Code', models.IntegerField(null=True)),
                ('PhoneNo', models.IntegerField()),
                ('Kitchen', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=1000)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='add_item',
        ),
    ]
