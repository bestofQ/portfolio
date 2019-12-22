# Generated by Django 3.0 on 2019-12-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='这里写关于作品的简介', max_length=100),
        ),
    ]
