from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Manager(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) :
        return self.title
    
class Agent(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
    instagran = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    linkdin = models.CharField(max_length=250)
    twiter = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class ctaegory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class score(models.Model):
    count = models.IntegerField()
    def __str__(self):
        return str(self.count)
    
class tester(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    stars = models.ForeignKey(score,on_delete=models.DO_NOTHING)
    manager= models.ForeignKey(Manager,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    def countstar(self):
        return range(self.stars.count)