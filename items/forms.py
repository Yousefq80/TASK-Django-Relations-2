from django import forms
from .models import Item,Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=["name", "price", "image","category"]