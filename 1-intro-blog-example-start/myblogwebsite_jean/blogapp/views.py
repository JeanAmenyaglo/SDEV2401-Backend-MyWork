from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Welcome to Jean's Blog!") commented this out when i introduced the template file home.html, that way the home page will render the template instead of just showing the text.
    return render(request, "blogapp/home.html")
