from django.forms import ModelForm
from .models import Receipt, Account, ExpenseCategory


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = (
            'vendor',
            'total',
            'tax',
            'date',
            'category',
            'account'
        )


class CategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = (
            'name',
        )


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            'name',
            'number'
        )
