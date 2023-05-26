from django.urls import path
from . import views


urlpatterns = [
    path("menu-items", views.menu_items),
    path("menu-item/<int:pk>", views.SingleMenuItemsView.as_view()),
    path("menu", views.menu),
    path("", views.welcome),
]