from cgi import print_exception
from tabnanny import verbose
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    price = models.IntegerField(default=8, verbose_name='价格')
    pub_date = models.DateField(verbose_name='出版日期')
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'book'
    

class HeroInfo(models.Model):
    GNEDER_CHOICES = {
        (0, 'male'),
        (1, 'female'),
    }
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GNEDER_CHOICES, default=0, verbose_name='性别')
    hbook = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='图书')

    def __str__(self):
        return self.hname

    class Meta:
      db_table = 'heros'
      verbose_name = '英雄'

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    class Meta:
        db_table = 'publish'

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=32)  
          
    class Meta:
        db_table = 'author'