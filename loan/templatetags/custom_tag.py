from django import template
from loan.models import LoanModel, DebtModel
from accounts.models import CustomUserModel
from books.models import Book

register = template.Library()


@register.simple_tag
def sum_debt(user):
    custom_user = CustomUserModel.objects.get(user=user)
    debt = DebtModel.objects.filter(user=custom_user)
    l = []
    for obj in debt:
        l.append(int(obj.amount))
        
    listSum = sum(l)
    return listSum


@register.simple_tag
def amount(user, book):
    custom_user = CustomUserModel.objects.get(user=user)
    debt = DebtModel.objects.get(user=custom_user, book_id=book)
    
    return debt.amount
