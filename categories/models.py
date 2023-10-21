from typing import Any
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return "Category: " + str(self.id) + " Parent: " + str(self.parent_id) if self.parent_id else "Root Category"
    # def __str__(self):
    #     return  "Node: " + (str(self.pk)) + ("Child of: " + str(self.parent_id)) if self.parent_id else "Root Node"

