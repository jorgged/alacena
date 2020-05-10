from django import forms
from .models import ProductModel, GroupProductModel, ShoppingCartModel


class GroupProductForm(forms.ModelForm):

    class Meta:
        model = GroupProductModel
        fields = ('name',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ('name', 'group', 'quantity',)


class ShoppingCartForm(forms.ModelForm):

    class Meta:
        model = ShoppingCartModel
        fields = ('Product', 'Check',)
