from django.contrib import admin
from .models import Account, ExpenseCategory, Receipt


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'vendor',
        'total',
        'tax',
    )
