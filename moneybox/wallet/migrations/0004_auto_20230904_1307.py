# Generated by Django 3.2 on 2023-09-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20230904_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='nominal',
            field=models.CharField(default='0', help_text='Currency denomination for exchange rate conversion', max_length=15, verbose_name='Currency Nominal for rates'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='value',
            field=models.CharField(default='0', help_text='Currency value for exchange rate"', max_length=15, verbose_name='Currency exchange rate'),
        ),
    ]
