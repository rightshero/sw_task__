from django.db import models


class Category(models.Model):
    type = models.CharField(max_length=100)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',null=True,blank=True)
    
    def __str__(self):
        return  "Node: " + (str(self.pk)) + ("Child of: " + str(self.parent_id)) if self.parent_id else "Root Node"

