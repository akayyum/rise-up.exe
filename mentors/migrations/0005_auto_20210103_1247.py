# Generated by Django 2.1.5 on 2021-01-03 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0004_auto_20210103_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentors',
            old_name='area',
            new_name='certifications',
        ),
    ]