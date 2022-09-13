from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория расходов'
        verbose_name_plural = 'Категории расходов'


class Expense(models.Model):
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=models.DateTimeField(auto_now_add=True), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Расход")
        verbose_name_plural = ("Расходы")

