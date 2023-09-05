from django.db import migrations


def forwards_func(apps, schema_editor):
    Currency = apps.get_model("wallet.models.currency", "Currency")
    Currency.objects.update_or_create(code="RUB", name="Российский рубль", nominal="1", value="1")


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20230904_1307'),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
