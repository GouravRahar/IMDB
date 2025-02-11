from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Movie(models.Model):
    budget = models.BigIntegerField(null=True,blank=True)
    homepage = models.CharField(max_length=1048,null=True,blank=True)
    original_language = models.CharField(max_length=1048,null=True,blank=True)
    original_title = models.CharField(max_length=1048,null=True,blank=True)
    overview = models.TextField(max_length=1048,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    revenue = models.BigIntegerField(blank=True,null=True)
    runtime = models.IntegerField(default=0,blank=True,null=True)
    status = models.CharField(max_length=1048,null=True,blank=True)
    title = models.CharField(max_length=1048,null=True,blank=True)
    vote_average = models.FloatField(default=0,null=True,blank=True)
    vote_count = models.IntegerField(default=0,null=True,blank=True)
    production_company_id = models.IntegerField(null=True,blank=True)
    genre_id = models.IntegerField(null=True,blank=True)
    languages = ArrayField(models.CharField(max_length=200), blank=True,default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

