# Generated by Django 3.2 on 2023-08-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('code', models.CharField(help_text="The unique code for this currency,e.g. 'USD' for US dollars", max_length=3, unique=True, verbose_name='Currency Code')),
                ('name', models.CharField(help_text='The name of the currency, e.g. "US Dollar"', max_length=255, verbose_name='Currency Name')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('name', models.CharField(db_index=True, help_text='Name of the group', max_length=255, verbose_name='Group name')),
                ('members', models.ManyToManyField(db_index=True, help_text='Members of the group', related_name='groups', to='users.Profile', verbose_name='Group members')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('name', models.CharField(db_index=True, help_text='Name of the wallet', max_length=255, verbose_name='Name')),
                ('balance', models.DecimalField(decimal_places=2, help_text='Current balance of the wallet', max_digits=10, verbose_name='Balance')),
                ('created_by', models.ForeignKey(help_text='Owner of the wallet', on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='User')),
                ('currency', models.ForeignKey(help_text='Currency of the wallet', on_delete=django.db.models.deletion.CASCADE, to='wallet.currency', verbose_name='Currency')),
                ('group', models.ForeignKey(help_text='Group that the wallet belongs to', on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('amount', models.DecimalField(decimal_places=2, help_text='The amount of money transferred.', max_digits=10, verbose_name='Transfer Amount')),
                ('comment', models.CharField(blank=True, help_text='Additional comment about the transfer (optional).', max_length=255, null=True, verbose_name='Transfer Comment')),
                ('created_by', models.ForeignKey(help_text='The user who made the transfer.', on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='User')),
                ('from_wallet', models.ForeignKey(help_text='The wallet from which the transfer is made.', on_delete=django.db.models.deletion.CASCADE, related_name='transfers_from', to='wallet.wallet', verbose_name='From Wallet')),
                ('group', models.ForeignKey(help_text='The group to which the transfer belongs.', on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group')),
                ('to_wallet', models.ForeignKey(help_text='The wallet to which the transfer is made.', on_delete=django.db.models.deletion.CASCADE, related_name='transfers_to', to='wallet.wallet', verbose_name='To Wallet')),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transfers',
            },
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('name', models.CharField(db_index=True, help_text='Name of the income category', max_length=255, verbose_name='Name')),
                ('created_by', models.ForeignKey(help_text='Profile that created the income category', on_delete=django.db.models.deletion.CASCADE, related_name='income_categories', to='users.profile', verbose_name='Created by')),
                ('group', models.ForeignKey(help_text='Group that the income category belongs to', on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Income Category',
                'verbose_name_plural': 'Income Categories',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Income amount')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Comment on income')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.incomecategory', verbose_name='Income category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Income creator')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group for income')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet', verbose_name='Wallet for income')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Incomes',
            },
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('name', models.CharField(db_index=True, help_text='The name of the expense category', max_length=255, verbose_name='Name')),
                ('created_by', models.ForeignKey(help_text='The user who created this expense category', on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='User')),
                ('group', models.ForeignKey(help_text='The group this expense category belongs to', on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Expense Category',
                'verbose_name_plural': 'Expense Categories',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount of expense')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Comment on expense')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.expensecategory', verbose_name='Expense category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='User who made the expense')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.group', verbose_name='Group related to the expense')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet', verbose_name='Wallet used for the expense')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date and time of creation', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Date and time of last update', verbose_name='Updated at')),
                ('rate', models.DecimalField(decimal_places=4, help_text='The rate at which the source currencycan be exchanged for the target currency.', max_digits=10, verbose_name='Exchange Rate')),
                ('source_currency', models.ForeignKey(help_text='The currency from whichthe exchange rate is being calculated.', on_delete=django.db.models.deletion.CASCADE, related_name='source_currency', to='wallet.currency', verbose_name='Source Currency')),
                ('target_currency', models.ForeignKey(help_text='The currency to whichthe exchange rate is being calculated.', on_delete=django.db.models.deletion.CASCADE, related_name='target_currency', to='wallet.currency', verbose_name='Target Currency')),
            ],
            options={
                'verbose_name': 'Currency rate',
                'verbose_name_plural': 'Currency rates',
            },
        ),
    ]
