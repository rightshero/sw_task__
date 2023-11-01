from django.db import models
from autoslug import AutoSlugField
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.






class Category(MPTTModel):
    parent = TreeForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = 
    True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    level=models.IntegerField()
    is_checked = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.parent is None:
            self.level=1
            
        elif self.parent.title.count('SUB ') == 0:
            
            self.level=self.parent.level+1
            
        else:
            
            self.level=self.parent.level+1
            
        super().save(*args, **kwargs)
        return self.level

        


            
    
    def __str__(self):
        return self.title

    class MPTTMeta:
        
        order_insertion_by=['created_at']
 
       
       
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

 
