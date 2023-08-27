from django.contrib import admin


class WalletAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id',
        'created_at',
        'updated_at',
        'name',
        'balance',
        'created_by',
        'group',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'created_by',
        'group',
        'id',
        'name',
        'balance',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
=======
        "id",
        "created_at",
        "updated_at",
        "name",
        "balance",
        "created_by",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "created_by",
        "group",
        "id",
        "name",
        "balance",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"
>>>>>>> upstream/main
