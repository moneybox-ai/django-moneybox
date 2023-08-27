from django.contrib import admin


class TransferAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id',
        'created_at',
        'updated_at',
        'from_wallet',
        'to_wallet',
        'amount',
        'comment',
        'created_by',
        'group',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'from_wallet',
        'to_wallet',
        'created_by',
        'group',
        'id',
        'amount',
        'comment',
    )
    date_hierarchy = 'created_at'
=======
        "id",
        "created_at",
        "updated_at",
        "from_wallet",
        "to_wallet",
        "amount",
        "comment",
        "created_by",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "from_wallet",
        "to_wallet",
        "created_by",
        "group",
        "id",
        "amount",
        "comment",
    )
    date_hierarchy = "created_at"
>>>>>>> upstream/main
