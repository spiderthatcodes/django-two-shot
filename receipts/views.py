from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt, ExpenseCategory, Account
from .forms import ReceiptForm


@login_required(login_url='/accounts/login/')
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts
    }
    return render(request, 'receipts/list.html', context)


@login_required(login_url='/accounts/login/')
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()

    context = {
        "form": form
    }

    return render(request, 'receipts/create.html', context)


@login_required(login_url='/accounts/login/')
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    receipts = Receipt.objects.filter(purchaser=request.user)

    context = {
        "categories": categories,
        "receipts": receipts
    }
    return render(request, 'receipts/cat_list.html', context)


@login_required(login_url='/accounts/login/')
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    receipts = Receipt.objects.filter(purchaser=request.user)

    context = {
        "accounts": accounts,
        "receipts": receipts
    }
    return render(request, 'receipts/account_list.html', context)
