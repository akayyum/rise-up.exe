# Generated by Django 2.1.5 on 2021-01-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0008_auto_20210103_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentors',
            name='upbringing',
            field=models.TextField(default='Location of initial upbringing: '),
        ),
    ]
