# Generated by Django 3.2 on 2023-09-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_alter_invite_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='invite_code',
            field=models.IntegerField(unique=True),
        ),
    ]
