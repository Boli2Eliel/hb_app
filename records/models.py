from django.db import models


class Formule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120)
    formule = models.ForeignKey(Formule, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name="Formule")
    uom = models.ForeignKey("UOM", on_delete=models.CASCADE, related_name='products', verbose_name="Unité")
    price_per_unit = models.FloatField()

    def __str__(self):
        return f"{self.name}/{self.formule.name}"

class UOM(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name