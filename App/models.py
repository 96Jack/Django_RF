from cgi import print_exception
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    price = models.IntegerField(default=8, verbose_name='价格')
    pub_date = models.DateField(verbose_name='出版日期')
    
    class Meta:
        db_table = 'book'