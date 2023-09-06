# Generated by Django 3.2 on 2023-09-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='cbr_valute_id',
            field=models.CharField(default=' ', help_text='Currency id needed to get valute rates', max_length=15, verbose_name='Currency id exchange rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='nominal',
            field=models.CharField(default='0', help_text='Currency denomination for exchange rate conversion', max_length=8, verbose_name='Currency Nominal for rates'),
        ),
        migrations.AddField(
            model_name='currency',
            name='value',
            field=models.CharField(default='0', help_text='Currency value for exchange rate"', max_length=15, verbose_name='Currency exchange rate'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(help_text='The unique code for this currency', max_length=3, unique=True, verbose_name='Currency Code'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(help_text='The name of the currency, e.g. US Dollar', max_length=255, verbose_name='Currency Name'),
        ),
    ]
