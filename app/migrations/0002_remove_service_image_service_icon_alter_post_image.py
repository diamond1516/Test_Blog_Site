# Generated by Django 4.2.1 on 2023-06-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default=111, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/'),
        ),
    ]
