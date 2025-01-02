from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Deal(models.Model):
    STAGE_CHOICES = [
        ('NEW', 'New Lead'),
        ('CONTACT', 'Contacted'),
        ('QUALIFY', 'Qualified'),
        ('QUOTE', 'Quote Sent'),
        ('CLOSE', 'Closed'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.customer.name}"