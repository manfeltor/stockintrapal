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

    method = forms.ChoiceField(
        choices=METHOD_CHOICES,
        label="Método de ingreso"
    )
    quality = forms.ChoiceField(
        choices=QUALITY_CHOICES,
        required=False,
        label="Calidad"
    )
    quantity = forms.IntegerField(
        min_value=1,
        label="Cantidad"
    )


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

    method = forms.ChoiceField(
        choices=METHOD_CHOICES,
        label="Método de salida"
    )
    quality = forms.ChoiceField(
        choices=QUALITY_CHOICES,
        required=False,
        label="Calidad"
    )
    quantity = forms.IntegerField(
        min_value=1,
        label="Cantidad"
    )


class ResetStockForm(forms.Form):
    QUALITY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('', 'Sin calidad'),
    ]

    quality = forms.ChoiceField(
        choices=QUALITY_CHOICES,
        required=False,
        label="Calidad"
    )
    quantity = forms.IntegerField(
        min_value=1,
        label="Cantidad"
    )
