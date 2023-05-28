from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .thorottles import TenCallsPerMin

# from rest_framework_csv.renderers import CSVRenderer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ["price", "title"]
    search_fields = ["title"]


# @api_view(["GET", "POST"])
# def menu_items(request):
#     if request.method == "GET":
#         items = MenuItem.objects.all()
#         to_price = request.query_params.get("to_price")
#         title = request.query_params.get("title")
#         ordering = request.query_params.get("ordering")
#         perpage = request.query_params.get("perpage", default=2)
#         page = request.query_params.get("page", default=1)
#         if to_price:
#             items = items.filter(price__gte=to_price)
#         if title:
#             items = items.filter(title__icontains=title)
#         if ordering:
#             ordering_fields = ordering.split(",")
#             items = items.order_by(*ordering_fields)
#         paginator = Paginator(items, perpage)
#         try:
#             items = paginator.page(page)
#         except EmptyPage:
#             items = []
#         serialized_item = MenuItemSerializer(items, many=True)
#         return Response(serialized_item.data)
#     elif request.method == "POST":
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors)


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


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response("You found the secret page!")


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(requests):
    # cheking if the user is a manager
    if requests.user.groups.all().filter(name="Manager").exists():
        return Response({"message": "Welcome to the manager page."})
    else:
        return Response(
            {
                "message": "Your are not a manager. You are not able to consume this endpoint."
            },
            status=status.HTTP_403_FORBIDDEN,
        )


@api_view()
@throttle_classes(
    [AnonRateThrottle]
)  # anonymous user can only access this endpoint 20 times per day
def throttle_check(request):
    return Response({"message": "Successful!"})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes(
    [TenCallsPerMin]
)  # authenticated user can only requests this endpoint 2 times per minute
def throttle_check_auth(request):
    return Response({"message": "Successful!"})
