from .models import Book
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def book_list(request):
    objects = Book.objects.all().values("id", "name", "thumb", "pdf").order_by('-id')
    data = list(objects)
    return JsonResponse(data, safe=False)

