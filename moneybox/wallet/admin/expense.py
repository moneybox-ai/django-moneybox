from django.contrib import admin


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id',
        'created_at',
        'updated_at',
        'name',
        'group',
        'created_by',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'group',
        'created_by',
        'id',
        'name',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
=======
        "id",
        "created_at",
        "updated_at",
        "name",
        "group",
        "created_by",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "group",
        "created_by",
        "id",
        "name",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"
>>>>>>> upstream/main


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
        'id',
        'created_at',
        'updated_at',
        'amount',
        'category',
        'comment',
        'created_by',
        'wallet',
        'group',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'category',
        'created_by',
        'wallet',
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
        "amount",
        "category",
        "comment",
        "created_by",
        "wallet",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "category",
        "created_by",
        "wallet",
        "group",
        "id",
        "amount",
        "comment",
    )
    date_hierarchy = "created_at"
>>>>>>> upstream/main
