from django.shortcuts import render

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
        err=None
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        if not name.isalpha():
            err="please right name enter...."
        if not message.isalpha():
            err="please right message enter...."
        if err:
            return render(request, 'index.html', {'err':err,'name':name,'message':message})
        data=Contact(name=name,email=email,text_area=message)
        data.save()
        grey_err=None
        grey_err="Form submission successful! Thank you for your submission."
        return render(request, 'index.html', {'grey_err':grey_err})
    return render(request, 'index.html',data)
def service(request):
    details=Service.objects.all()
    return render(request, 'service.html',{'details':details})