# Generated by Django 3.2.6 on 2021-11-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0019_auto_20211123_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='decklistzone',
            name='show_by_default',
            field=models.BooleanField(default=False),
        ),
    ]
