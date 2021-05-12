from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
import uuid
from tinymce.models import HTMLField
# Create your models here.





class Post(models.Model):

    title = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='pics')
    intro = models.TextField()
    blog = HTMLField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(default = timezone.now)
    likes = models.IntegerField(default=0)

    class Meta:

        ordering = ['-timestamp']
            

    def __str__(self):

        return self.title

   
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_img = models.ImageField(default='default.jpg',upload_to='profilepics')
    name = models.CharField(max_length=200,null=True,blank=True,unique=True)
    post = models.ManyToManyField(Post,blank=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):

        return f'{self.user.username} Profile'
