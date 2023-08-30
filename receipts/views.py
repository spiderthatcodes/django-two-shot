from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Receipt


@login_required(login_url='/accounts/login/')
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts
    }
    return render(request, 'receipts/list.html', context)
