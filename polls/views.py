from django.shortcuts import render
from django.http import HttpResponse

# Index function: Called upon opening homepage
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

