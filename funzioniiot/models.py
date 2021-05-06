from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class Titoli2(models.Model):
    codtit2 = models.CharField(max_length=250)
    codslugtit2 = models.SlugField(max_length=250,unique_for_date='codcreatedtit2')
    codauthortit2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_titoli2')                  
    codisintit2= models.CharField(max_length=250) 
    codbodytit2 = models.TextField()
    codpublishtit2= models.DateTimeField(default=timezone.now)
    codcreatedtit2 = models.DateTimeField(auto_now_add=True)
    codupdatedtit2 = models.DateTimeField(auto_now=True)
    codmintit2 = models.FloatField()
    codmaxtit2 = models.FloatField()
   
    def __str__(self):
        return self.codtit2

    def get_absolute_url(self):
        return reverse("titolo_detail",  kwargs ={"pk":self.pk})
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Giornalista(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=40)

    def __str__(self):
        return  self.nome + self.cognome

class Cliente(models.Model):
    codcli = models.CharField(max_length=20)
    descli = models.CharField(max_length=60)
    citcli = models.CharField(max_length=60)
    capcli = models.CharField(max_length=60)
   
    def __str__(self):
        return  self.codcli + self.descli

    def get_absolute_url(self):
        return reverse("cliente_detail",  kwargs ={"pk":self.pk})


