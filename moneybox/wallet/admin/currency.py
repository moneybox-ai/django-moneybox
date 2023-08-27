from django.contrib import admin


class CurrencyAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'created_at', 'updated_at', 'code', 'name')
    list_filter = ('created_at', 'updated_at', 'id', 'code', 'name')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
=======
    list_display = ("id", "created_at", "updated_at", "code", "name")
    list_filter = ("created_at", "updated_at", "id", "code", "name")
    search_fields = ("name",)
    date_hierarchy = "created_at"
>>>>>>> upstream/main


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id',
        'created_at',
        'updated_at',
        'source_currency',
        'target_currency',
        'rate',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'source_currency',
        'target_currency',
        'id',
        'rate',
    )
    date_hierarchy = 'created_at'
=======
        "id",
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "rate",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "id",
        "rate",
    )
    date_hierarchy = "created_at"
>>>>>>> upstream/main
