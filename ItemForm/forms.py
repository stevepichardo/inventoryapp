from django import forms
from datetime import datetime 
from . import models

class ItemForm(forms.ModelForm):
    class Meta: 
        model = models.Item
        fields = ('description', 'cost', 'item_type', 'sold_price')


# use it for saving data