# Generated by Django 3.2.5 on 2022-05-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_newpost_posttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='postImg',
            field=models.ImageField(blank=True, default='pic02.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='postTime',
            field=models.TextField(default='03:16PM'),
        ),
    ]
