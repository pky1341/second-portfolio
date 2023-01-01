from .models import About, Achivement, Home, Information, Navbar,Project, Service, Webtype
from django.contrib import admin

admin.site.register(Navbar)

class AdminNavbar(admin.ModelAdmin):
    list_display=['navlogo','pagetitle']
    
admin.site.register(Home)

class AdminHome(admin.ModelAdmin):
    list_display=['home_sm_img','home_lg_img','sec_heading','upload_date']
    
admin.site.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display=['illustration_img','my_dp','little_desc','upload_date']
admin.site.register(Information)
class AdminInformation(admin.ModelAdmin):
    list_display=['per_key','per_value']
admin.site.register(Achivement)
class AdminInformation(admin.ModelAdmin):
    list_display=['Years_of_Experiences','Happy_Customers','Project_Finished','Digital_Awards']
    
admin.site.register(Project)

class AdminProject(admin.ModelAdmin):
    list_display=['project_name','project_img']
    
admin.site.register(Webtype)
class AdminWebtype(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Service)
class AdminService(admin.ModelAdmin):
    list_display=['web_type','web_pic','web_name','web_desc','web_url']