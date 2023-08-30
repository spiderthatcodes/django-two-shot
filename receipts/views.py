from django.shortcuts import render
from .models import Receipt


def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts": receipts
    }
    return render(request, 'receipts/list.html', context)
