# Generated by Django 3.0.3 on 2021-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0034_auto_20201116_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='rules',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
