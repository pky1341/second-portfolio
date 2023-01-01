from django.shortcuts import render

from mysite_app.models import About, Achivement, Home, Information, Navbar,Project, Service


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
    return render(request, 'index.html',data)
def service(request):
    details=Service.objects.all()
    return render(request, 'service.html',{'details':details})