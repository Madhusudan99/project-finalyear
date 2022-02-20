from datetime import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Credit(models.Model):
    creation_timestamp = models.DateTimeField(default=timezone.now)
    credit_amount = models.PositiveBigIntegerField()
    account_holder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.account_holder.username

class Transaction(models.Model):
    account_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_timestamp = models.DateTimeField(default=timezone.now)
    deposit_amount = models.PositiveBigIntegerField()
    # outstanding_credit = models.ForeignKey(Credit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.account_holder.username
