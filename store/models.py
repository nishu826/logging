from django.db import models

# Create your models here.
class Store(models.Model):
    part_number = models.CharField(max_length=10)
    purchase_order =models.PositiveIntegerField()
    mat_code = models.PositiveIntegerField()
    description= models.CharField(max_length=37)
    quantity=models.PositiveIntegerField()
    qty_consumed=models.PositiveIntegerField()
    location=models.CharField(max_length=50)
    gate_pass=models.PositiveIntegerField()
    Date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True) 
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return f'Store :{self.part_number}'