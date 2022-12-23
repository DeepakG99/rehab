from django.shortcuts import render

#Index Page
def Index(request):
    context = {

    }
    return render(request,"index.html",context)



# ABout us page
def AboutUs(request):
    context = {

    }
    return render(request,"about.html", context)


#Services Page
def Services(request):
    context = {

    }
    return render(request, "service.html", context)


# contactUs page
def ContactUs(request):
    context = {

    }
    return render(request, "contact.html", context)


#team page
def OurTeam(request):
    context = {

    }
    return render(request, "team.html", context)


#Testemonial Page
def Testimonial(request):
    context = {

    }
    return render(request, "testimonial.html", context)

#Appointment Page
def Appointment(request):
    context = {

    }
    return render(request, "index.html", context)

#Apply Page
def ApplyUS(request):
    context = {

    }
    return render(request, "apply.html", context)

#error Page
def ErrorPage(request):
    context = {

    }
    return render(request, "404.html", context)

#benefit pages

def Benefit(request):
    context = {

    }
    return render(request, "feature.html", context)





