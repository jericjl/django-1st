import random                   # Allows to create random Value dependencies
import os                       # required when using or calling os.path function dependencies for PATH location handling
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

#for image upload Function
def get_filename_ext(filepath):             
    base_name = os.path.basename(filepath)  
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance , filename):         # this allows the image to renamed automatically in random numbers
    #print(instance)
    #print(filename)
    new_filename = random.randint(1,999999999999)
    name ,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
        )


class ProductQuerySet(models.query.QuerySet): # query set for featured products -> this also define in models manager
    def active(self):
        return self.filter(active=True)

    def featured(self):
        #value = self.filter(featured=True)
        #print(value)
        return self.filter(featured=True ,active =True)

    def search(self,query): #Good for search function
        lookups = (
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__name__icontains=query)
            )
        return self.filter(lookups).distinct()
    

# Model Manager

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db) # call the ProductQuerySet class ^
        def all(self):
            return self.get_queryset().active()
    
    # get value where id is equal from the user request
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        count = qs.count()
        if count == 1 and not None:
         #   print(count)
            return qs.first()
        return None

    def feature(self):
        q = self.get_queryset().featured()
        return q

    #get value with featured = True in database
    def features(self,id): # this is to filter featured products #Products.objects.featured()
        q = self.get_queryset().featured()
        instance = q.filter(id=id)
        count = instance.count()
        if count == 1 or not None:
            return instance.first() 
        return None
    #get value that uses slug value instead of ID or PK
    def get_by_slug(self,slug):
        qs = self.get_queryset().filter(slug = slug)
        count = qs.count()
        if count == 1 and not None:
            return qs.first
        return None

    def search(self,query):
        return self.get_queryset().active().search(query)


# Create your models here.
class Products(models.Model):
    name        = models.CharField(max_length = 200)
    slug        = models.SlugField()#(blank=True, null=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2 ,max_digits=65)
    image       = models.ImageField(upload_to =upload_image_path,null = True, blank =True) # imagefield requires pillow (install it using : pip install pillow)
    summary     = models.TextField(null=False)
    featured    = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now=True)
    active      = models.BooleanField(default=True)

    objects     =   ProductManager()

    def get_absolute_url(self):# This function will allow to use the {{obj.get_absolute_url}}
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:product-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name # Display Name of of the objects in the admin page

    #def __unicode__(self):
     #   return self.name

def product_pre_save_receiver(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender =Products)


    
