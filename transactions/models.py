from django.db import models


class Account(models.Model):
    name = models.TextField()


class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    trans_date = models.DateTimeField("transaction date")
    from_account = models.ForeignKey(Account, related_name="from_account", on_delete=models.RESTRICT)
    to_account = models.ForeignKey(Account, related_name="to_account", on_delete=models.RESTRICT)


class ExpenseCategory(models.Model):
    name = models.TextField()


class Expense(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.RESTRICT)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.RESTRICT)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
