from django.http import HttpResponse
from django.shortcuts import redirect, render

from mysite_app.models import About, Achivement, Contact, Home, Information, Navbar,Project, Service


def index(request):
    new=Navbar.objects.all()
    homepage=Home.objects.all()
    about=About.objects.all()
    inform=Information.objects.all()
    achive=Achivement.get_all_achivement()
    project=Project.objects.all()
    data={}
    data['new']=new
    data['homepage']=homepage
    data['about']=about
    data['inform']=inform
    data['achive']=achive
    data['project']=project
    
    if request.method=='POST':
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        context=Contact(name=name,email=email,text_area=message)
        context.save()
        success="<h1><strong>Success!</strong> Your form has been submitted successfully.</h1>"
        return HttpResponse(success)    
    return render(request, 'index.html',data)
    
    
def service(request):
    details=Service.objects.all()
    return render(request, 'service.html',{'details':details})