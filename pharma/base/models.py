from django.db import models


CATEGORY = (
('Cream', 'Cream'),
('Tablet', 'Tablet'),
('Syrup', 'Syrup'),
('Injection', 'Injection'),

)

class tag(models.Model):
    name = models.CharField(max_length=50, null=True,)

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
    stock = models.PositiveIntegerField()
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, blank=True, null=True, choices=CATEGORY)
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(tag)


    def __str__(self):
        return self.name

class sell(models.Model):
    # Cat = (
    #     ('Cream', 'Cream'),
    #     ('Tablet', 'Tablet'),
    #     ('Syrup', 'Syrup'),
    #     ('Injection', 'Injection'),

    # )
    sell_name = models.ForeignKey(product, on_delete=models.CASCADE, default=1)
    sell_price = models.FloatField(null=True)
    sell_quantity = models.PositiveIntegerField( blank=True)
    sell_cat = models.CharField(max_length=100, blank=True, null=True, choices=CATEGORY)
    sell_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sell_name.name
