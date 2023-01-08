from django.shortcuts import render, redirect
from .models import *

#Index Page
def Index(request):
    banner = BannerImage.objects.all()
    member = TeamMember.objects.all()
    service = Service.objects.all()
    context = {
        "banner":banner,
        "member":member,
        "service":service
    }
    return render(request,"index.html",context)


def Appointment_req(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        atime = request.POST["time"]
        medium = request.POST["medium"]
        message = request.POST["message"]

        appoint = Appointment(name=name, email=email, mobile=number,atime=atime,medium=medium,reason=message)
        appoint.save()
        return redirect('index')
    return render(request, "index.html")

#Apply Page
def ApplyUS(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        resume = request.FILES["resume_file"]

        apply = ResumeUpload(name=name,mobile=number,email=email,Resume=resume)
        apply.save()
        return redirect('index')
    return render(request, "index.html")









