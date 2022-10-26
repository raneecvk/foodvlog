from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
            return'{}'.format(self.name)
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    price=models.IntegerField()
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    
    def __str__(self):
        return'{}'.format(self.name)
    
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])