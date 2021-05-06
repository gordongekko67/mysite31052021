from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')
 


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.         
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])




class Comment(models.Model):
    # very important the foreign  key to refer to a post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'











class Articoli(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    codart = models.CharField(max_length=250)
    codslug = models.SlugField(max_length=250,
                            unique_for_date='codpublish')
    codauthor = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_articolo')
    codbody = models.TextField()
    codpublish = models.DateTimeField(default=timezone.now)
    codcreated = models.DateTimeField(auto_now_add=True)
    codupdated = models.DateTimeField(auto_now=True)
    codstatus = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    class Meta:
        ordering = ('-codpublish',)
    def __str__(self):
        return self.codart



class Clienti(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    codcli = models.CharField(max_length=250)
    codslugcli = models.SlugField(max_length=250,
                            unique_for_date='codpublishcli')
    codauthorcli = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_clienti')
    codbodycli = models.TextField()
    codpublishcli = models.DateTimeField(default=timezone.now)
    codcreatedcli = models.DateTimeField(auto_now_add=True)
    codupdatedcli = models.DateTimeField(auto_now=True)
    codstatuscli = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    class Meta:
        ordering = ('-codpublishcli',)
    def __str__(self):
        return self.codcli


class Titoli(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    codtit = models.CharField(max_length=250)
    codslugtit = models.SlugField(max_length=250,unique_for_date='codcreatedtit')
    codauthortit = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_titoli')                  
    codisintit= models.CharField(max_length=250) 
    codbodytit = models.TextField()
    codpublishtit= models.DateTimeField(default=timezone.now)
    codcreatedtit = models.DateTimeField(auto_now_add=True)
    codupdatedtit = models.DateTimeField(auto_now=True)
    codmintit = models.FloatField()
    codmaxtit = models.FloatField()
    codobjects = models.Manager() # The default manager.
    codpublished = PublishedManager() # Our custom manager.    
   
    class Meta:
        ordering = ('-codcreatedtit',)
    def __str__(self):
        return self.codtit





