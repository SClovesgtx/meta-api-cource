from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(["GET", "POST"])
def books(request):
    return Response("List of books", status=status.HTTP_200_OK)


class BookList(APIView):
    def get(self, request):
        author = request.GET.get("author")
        if author:
            return Response(
                {"message": f"List of books of author {author}."},
                status=status.HTTP_200_OK,
            )
        return Response({"message": "List of books"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "new book created"}, status=status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        return Response(
            {"message": f"Single book with id {pk}."}, status=status.HTTP_200_OK
        )
