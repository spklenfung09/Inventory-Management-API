from django import forms

from inventory.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class QueryForm(forms.Form):
    query = forms.CharField(required=False)
    query_by = forms.CharField()
    query_limit = forms.IntegerField(initial=100, required=False)
    order_by = forms.CharField(empty_value='pk')
    order_type = forms.ChoiceField(choices=[
        ('desc', 'desc'),
        ('ascn', 'ascn')
    ], required=False)
