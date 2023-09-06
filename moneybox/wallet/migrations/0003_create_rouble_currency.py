from django.db import migrations


def forwards_func(apps, schema_editor):
    Currency = apps.get_model("wallet", "Currency")
    db_alias = schema_editor.connection.alias
    Currency.objects.using(db_alias).update_or_create(code="RUB", name="Российский рубль")


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20230906_0655'),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
