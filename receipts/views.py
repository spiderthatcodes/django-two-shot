from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt
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
