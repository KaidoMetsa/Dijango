from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
