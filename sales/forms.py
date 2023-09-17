from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class AddSalesPointForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Point de vente", "class": "form-control fw-semibold"}), label="")

    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Adresse", "class": "form-control fw-semibold"}), label="")

    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Email", "class": "form-control fw-semibold"}), label="")

    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Téléphone", "class": "form-control fw-semibold"}), label="")

    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "BP", "class": "form-control fw-semibold"}), label="")

    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Ville", "class": "form-control fw-semibold"}), label="")

    # country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pays", "class":"form-control fw-semibold"}), label="")

    class Meta:
        model = SalesPoint
        exclude = ("updated_at", "created_at",)
