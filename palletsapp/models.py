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

    quality = models.CharField(max_length=1, choices=QUALITY_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('quality', 'status')
        verbose_name = 'Pallet Stock'
        verbose_name_plural = 'Pallet Stocks'

    def __str__(self):
        return f"{self.get_quality_display()} - {self.get_status_display()} : {self.quantity}"
    
class PalletLog(models.Model):
    ACTION_CHOICES = [
        ('stock_in', 'Stock In'),
        ('stock_out', 'Stock Out'),
        ('reset', 'Reset Stock'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=150)  # No FK, immutable
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    payload = models.JSONField()  # Full snapshot

    def __str__(self):
        return f"{self.timestamp} | {self.username} | {self.action}"