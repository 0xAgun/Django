from django.db import models


class tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    Cat = (
        ('Cream', 'Cream'),
        ('Tablet', 'Tablet'),
        ('Syrup', 'Syrup'),
        ('Injection', 'Injection'),

    )
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100, blank=True)
    stock = models.CharField(max_length=100, blank=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=Cat)
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(tag)


    def __str__(self):
        return self.name

class sell(models.Model):
    Cat = (
        ('Cream', 'Cream'),
        ('Tablet', 'Tablet'),
        ('Syrup', 'Syrup'),
        ('Injection', 'Injection'),

    )
    namess = models.ForeignKey(product, on_delete=models.CASCADE)
    sell_quantity = models.CharField(max_length=100, blank=True)
    sell_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.namess
