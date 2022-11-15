from django import forms

CATEGORY_CHOICES = [("other", "Разное"), ('unique', 'Уникальные'), ('priority', 'Приоритетные'),  ('basic', 'Базовые')]


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='name')
    description = forms.CharField(widget=forms.Textarea, label='description')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    remainder = forms.IntegerField(min_value=0, required=True, label='remainder')
    price = forms.DecimalField(decimal_places=2, required=True, label='price')