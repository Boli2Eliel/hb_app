from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class AddProductForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Nom du produit", "class": "form-control fw-semibold"}), label="")

    # country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pays", "class":"form-control fw-semibold"}), label="")

    class Meta:
        model = Product
        exclude = ("updated_at", "created_at",)

class AddFormuleForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Nom de la formule", "class": "form-control fw-semibold"}), label="")

    # country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pays", "class":"form-control fw-semibold"}), label="")

    class Meta:
        model = Formule
        exclude = ("updated_at", "created_at",)


class AddUomForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Nom de l'unité'", "class": "form-control fw-semibold"}), label="")

    # country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pays", "class":"form-control fw-semibold"}), label="")

    class Meta:
        model = Uom
        exclude = ("updated_at", "created_at",)


