from django.db import models

class ConvertedFile(models.Model):
  original_file = models.FileField(upload_to='uploads/')
  converted_pdf = models.FileField(upload_to='pdfs/', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
