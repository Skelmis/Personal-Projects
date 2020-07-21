# Generated by Django 3.0.5 on 2020-07-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200704_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(default='b_map3.png', upload_to='partnerPictures')),
            ],
        ),
        migrations.DeleteModel(
            name='PartnerModel',
        ),
    ]