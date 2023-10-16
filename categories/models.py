from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.parent:
            return f"{self.parent.get_full_name()} > {self.name}"
        else:
            return self.name
        
    class Meta:
        verbose_name_plural = "Categories"

