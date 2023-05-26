from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status

# from rest_framework_csv.renderers import CSVRenderer


# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


@api_view(["GET", "POST"])
def menu_items(request):
    if request.method == "GET":
        items = MenuItem.objects.all()
        to_price = request.query_params.get("to_price")
        title = request.query_params.get("title")
        ordering = request.query_params.get("ordering")
        if to_price:
            items = items.filter(price__gte=to_price)
        if title:
            items = items.filter(title__icontains=title)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == "POST":
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({"data": serialized_item.data}, template_name="menu-items.html")


@api_view(["GET"])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = "<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>"
    return Response(data)
