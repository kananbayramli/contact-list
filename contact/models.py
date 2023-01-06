from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

