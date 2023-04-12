from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Book

# Create your views here.
@csrf_exempt
def books(request):
    if request.method == "GET":
        calledbooks = Book.objects.all().values()
        return JsonResponse({"books": list(calledbooks)})
    elif request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        book = Book(title, author, price)
        try:
            book.save()
        except:
            raise IntegrityError()
            return JsonResponse({"error": True, "message": "required field missing"}, status=400)
        return JsonResponse(model_to_dict(book), status=201)