from django.db import models

# Create your models here.
class SEO(models.Model):
    domain = models.TextField()
    visits = models.IntegerField()
   
   

    def __str__(self):
        return self.domain
 