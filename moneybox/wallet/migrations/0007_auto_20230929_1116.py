# Generated by Django 3.2 on 2023-09-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_auto_20230927_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='type',
            field=models.CharField(choices=[('fiat', 'fiat'), ('crypto', 'crypto')], default='fiat', help_text='The type of the currency, e.g. fiat or crypto', max_length=255, verbose_name='Currency Type'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(help_text='The unique code for this currency', max_length=10, unique=True, verbose_name='Currency Code'),
        ),
    ]