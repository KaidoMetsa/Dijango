from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Untitled"
