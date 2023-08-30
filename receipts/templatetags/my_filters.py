from django import template

register = template.Library()


@register.filter(name="cat_total")
def cat_receipt_total(rec, cat):
    return len(rec.filter(category=cat))


@register.filter(name="account_total")
def account_receipt_total(rec, account):
    return len(rec.filter(account=account))
