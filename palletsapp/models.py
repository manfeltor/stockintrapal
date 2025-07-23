from django.db import models

# Create your models here.
from django.db import models

class PalletStock(models.Model):
    QUALITY_CHOICES = [
        ('A', 'Calidad A'),
        ('B', 'Calidad B'),
    ]

    STATUS_CHOICES = [
        ('ok', 'OK'),
        ('scrap', 'Scrap'),
    ]

    quality = models.CharField(max_length=1, choices=QUALITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('quality', 'status')
        verbose_name = 'Pallet Stock'
        verbose_name_plural = 'Pallet Stocks'

    def __str__(self):
        return f"{self.get_quality_display()} - {self.get_status_display()} : {self.quantity}"
