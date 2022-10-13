from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#foreign k=call

#category table
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    desc = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name
   

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    pub_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, blank=True)

  

    img = models.ImageField()
    

    def __str__(self):
        return self.title
   