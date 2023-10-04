from django.db import models

# Create your models here.

class message(models.Model):
    massage_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self)
        return self.massage_text