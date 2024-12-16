from django.db import models

# Create your models here.

class Ticket(models.Model):
    submitter = models.CharField(max_length=100)
    body =models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submitter}: {self.body}"