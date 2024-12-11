from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    year = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)


    def __str__(self):
        return f"{self.brand.name} - {self.name}"