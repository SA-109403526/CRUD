from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Topic(models.Model):
#    name = models.CharField(max_length=200)
    
#    def __str__(self):
#        return self.name

#class Room(models.Model):
#    host= models.ForeignKey(User ,on_delete=models.SET_NULL,null = True)
#    topic= models.ForeignKey(Topic ,on_delete=models.SET_NULL,null = True)
#    name = models.CharField(max_length=200)
#    description = models.TextField(null=True,blank=True)
    #participants = 
#    updated = models.DateTimeField(auto_now = True)
#    created = models.DateTimeField(auto_now_add=True)
    
#    def __str__(self):
#        return self.name
    

# 建資料庫
class city(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class attraction(models.Model):
    city = models.ForeignKey(city ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class project(models.Model):
    member = models.ForeignKey(User,on_delete= models.CASCADE)
    city = models.ForeignKey(city ,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return self.name

class project_attraction(models.Model):
    project = models.ForeignKey(project,on_delete= models.CASCADE)
    attraction = models.ForeignKey(attraction ,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __foreignkey__(self):
        return self.attraction

class picture(models.Model):
    attraction = models.ForeignKey(attraction,on_delete= models.CASCADE)
    picture = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __foreignkey__(self):
        return self.attraction

