# Generated by Django 2.1.5 on 2021-02-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_remove_mentor_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='available',
            field=models.TextField(default='Yes', max_length=50),
        ),
    ]
