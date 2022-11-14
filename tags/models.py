from django.db import models
#this package will help us create generic relation ship between our models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #what tag is applied to what tag
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #we will create an attribute that define the tag type we could use "product" instead of content_type"
    #but in this case we want to create reusable module that we can use in article,vidoe,books not only in product 
    #s
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    