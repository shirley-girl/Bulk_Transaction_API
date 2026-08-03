from django.db import models

# Create your models here.
class Account(models.Model):
   
   name = models.CharField(max_length=20) 
   account_number = models.CharField(max_length=20) 

   def __str__(self):
       return self.name

class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('credit', 'Credit'),
         ('debit', 'Debit')
    ]

    reference = models.CharField(max_length=20) 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    transactio_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES) 
    description = models.CharField(max_length=50) 
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return self.reference 
