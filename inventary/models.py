from django.db import models


class GroupProductModel(models.Model):
    name = models.CharField(max_length=15, blank=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=15, blank=False)
    group = models.ForeignKey(GroupProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ShoppingCartModel(models.Model):
    Product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    Check = models.BooleanField(default=True)

