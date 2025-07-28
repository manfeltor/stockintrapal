# pallets/forms.py
from django import forms

class StockInForm(forms.Form):
    METHOD_CHOICES = [
        ('colecta', 'Colecta'),
        ('compra', 'Compra'),
        ('entrada_reparacion', 'Entrada Reparación'),
    ]
    QUALITY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('', 'Sin calidad'),
    ]

    method = forms.ChoiceField(choices=METHOD_CHOICES)
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, required=False)
    quantity = forms.IntegerField(min_value=1)


class StockOutForm(forms.Form):
    METHOD_CHOICES = [
        ('entrega_colecta', 'Entrega Colecta'),
        ('envio_reparar', 'Envío a Reparar'),
        ('venta', 'Venta'),
        ('descarte', 'Descarte'),
    ]
    QUALITY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('', 'Sin calidad'),
    ]

    method = forms.ChoiceField(choices=METHOD_CHOICES)
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, required=False)
    quantity = forms.IntegerField(min_value=1)


class ResetStockForm(forms.Form):
    QUALITY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('', 'Sin calidad'),
    ]

    quality = forms.ChoiceField(choices=QUALITY_CHOICES, required=False)
    quantity = forms.IntegerField(min_value=0)
