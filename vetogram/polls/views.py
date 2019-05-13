from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def package(request):
    return render(request,
                  template_name="polls/packages.html",
                  context={})
