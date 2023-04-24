from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Book

# Create your views here.
@api_view(["GET", "POST"])
def books(request):
    if request.method == "GET":
        calledbooks = Book.objects.all().values()
        return Response({"books": list(calledbooks)}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")
        book = Book(title, author, price)
        try:
            book.save()
        except:
            raise IntegrityError()
            return Response({"error": True, "message": "required field missing"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(book), status=status.HTTP_201_CREATED)