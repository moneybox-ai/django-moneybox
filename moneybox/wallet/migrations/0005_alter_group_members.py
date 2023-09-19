# Generated by Django 3.2 on 2023-09-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_apiuser_invite'),
        ('wallet', '0004_auto_20230917_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ForeignKey(help_text='Members of the group', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='users.apiuser', verbose_name='Group members'),
        ),
    ]
