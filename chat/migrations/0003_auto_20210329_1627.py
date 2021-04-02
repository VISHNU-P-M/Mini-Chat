# Generated by Django 3.1.7 on 2021-03-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='msg_type',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='pic_msg',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
