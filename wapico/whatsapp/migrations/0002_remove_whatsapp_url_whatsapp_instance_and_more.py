# Generated by Django 4.1.5 on 2023-01-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whatsapp',
            name='url',
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='instance',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='phone_number',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='token',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='whatsapp',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
