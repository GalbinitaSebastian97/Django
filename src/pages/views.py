from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World<h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    contact_dict = {
        "details" : " One detail about me"
    }
    return render(request, "contact.html", contact_dict)

def about_view(request, *args, **kwargs):
    my_dict = {
        "user" : "Galbinita Sebastian",
        "age" : "23"
    }
    return render(request, 'about.html', my_dict)