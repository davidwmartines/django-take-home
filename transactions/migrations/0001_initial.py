# Generated by Django 3.1.4 on 2020-12-22 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('trans_date', models.DateTimeField(verbose_name='transaction date')),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='from_account', to='transactions.account')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='to_account', to='transactions.account')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='transactions.expensecategory')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='transactions.transaction')),
            ],
        ),
    ]