# Generated by Django 3.1.7 on 2021-03-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210329_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='pic_msg',
        ),
        migrations.AddField(
            model_name='messages',
            name='upload_file',
            field=models.FileField(default='', null=True, upload_to='files'),
        ),
    ]
