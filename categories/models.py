from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # Automatically generated unique ID
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.name