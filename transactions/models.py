from django.db import models
from django.core.exceptions import ValidationError


class Account(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    trans_date = models.DateTimeField("transaction date")
    from_account = models.ForeignKey(
        Account, related_name="from_account", on_delete=models.RESTRICT
    )
    to_account = models.ForeignKey(
        Account, related_name="to_account", on_delete=models.RESTRICT
    )

    # def clean(self):
    #     if self.from_account is None:
    #         raise ValidationError("From Account not specified")
    #     if self.to_account is None:
    #         raise ValidationError("To Account not specified")
    #     if self.from_account.id == self.to_account.id:
    #         raise ValidationError("From Account and To Account cannot be the same.")

    def __str__(self):
        return f"{self.trans_date} {self.amount} {self.to_account.name}  ({self.from_account.name})"


class ExpenseCategory(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.RESTRICT)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.RESTRICT)
    amount = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return f"{self.category} {self.amount} {self.transaction.trans_date}"
