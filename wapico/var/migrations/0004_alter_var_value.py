# Generated by Django 4.1.5 on 2023-02-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var', '0003_alter_var_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='var',
            name='value',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
