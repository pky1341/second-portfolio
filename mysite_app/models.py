from django.db import models

class Navbar(models.Model):
    pagetitle=models.CharField(max_length=30, blank=True, null=True)
    navlogo=models.ImageField(upload_to='media' ,null=True,blank=True)
    
class Home(models.Model):
    home_sm_img=models.ImageField(upload_to='media/h_sm_img',null=True,blank=True)
    home_lg_img=models.ImageField(upload_to='media/h_lg_img',null=True,blank=True)
    sec_heading=models.CharField(max_length=100,null=True,blank=True)
    upload_date=models.DateField(null=True,blank=True)
class About(models.Model):
    illustration_img=models.ImageField(upload_to='media/illustration',null=True,blank=True)
    my_dp=models.ImageField(upload_to='media/my_DP',null=True,blank=True)
    little_desc=models.TextField(max_length=5000,null=True,blank=True)
    upload_date=models.DateField(null=True,blank=True)
    
class Information(models.Model):
    per_key=models.CharField(max_length=200,blank=True, null=True)
    per_value= models.CharField(max_length=200,blank=True, null=True)
    
    def __str__(self):
        return self.per_key
class Achivement(models.Model):
    Years_of_Experiences=models.IntegerField(default=0)
    Happy_Customers=models.IntegerField(default=0)
    Project_Finished=models.IntegerField(default=0)
    Digital_Awards=models.IntegerField(default=0)
    
    @staticmethod
    def get_all_achivement():
        return Achivement.objects.all()

class Project(models.Model):
    project_name=models.CharField(max_length=100,null=True,blank=True)
    project_img=models.ImageField(upload_to='media/project_img',null=True,blank=True)
    project_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.project_name