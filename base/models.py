from this import d
from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject
