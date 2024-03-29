from django.db import models
from accounts.models import CustomUserModel
from books.models import Book

from datetime import datetime, timedelta


class LoanModel(models.Model):
    LOAN_STATUS = (
        ('C', 'choosing'),
        ('S', 'started'),
        ('R', 'returned'),
        ('T', 'to_be_returned'),
    )
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.user.username} has {self.book} and loan is in {self.status} faze'


class DebtModel(models.Model):
    loan = models.OneToOneField(LoanModel, on_delete=models.CASCADE, related_name='loan_debt')
    amount = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount}'
    

        