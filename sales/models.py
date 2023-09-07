from django.db import models
from django_countries.fields import CountryField

from authentication.models import Account
from records.models import Product


class SalesPoint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, related_name='salespoints', on_delete=models.CASCADE, verbose_name='Créé par')
    name = models.CharField(max_length=150, verbose_name="Point de vente")
    address = models.CharField(max_length=100, verbose_name="Adresse")
    email = models.CharField(max_length=100, verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Téléphone")
    zipcode = models.CharField(max_length=20, verbose_name="BP", blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="Ville")
    country = CountryField(blank_label='(Choisir Pays)', verbose_name="Pays", )

    def __str__(self):
        return f"{self.name}/{self.city}"

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, related_name='orders', on_delete=models.CASCADE, verbose_name='Créé par')
    customer_name = models.CharField(max_length=150,verbose_name="Nom du client", null=True, blank=True, default="lambda")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders" ,verbose_name="Produit")
    qty = models.IntegerField(default=0)
    total = models.FloatField()
    sales_point = models.ForeignKey(SalesPoint, related_name='orders', on_delete=models.CASCADE, verbose_name="Point de vente", null=True, blank=True)

    def __str__(self):
        return f" commande-{self.product.name}/{self.customer_name}"
