from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    # This creates a column in the model that hold the id of the parent object
    # in this case we can have unlimited subcategories for a parent category
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name