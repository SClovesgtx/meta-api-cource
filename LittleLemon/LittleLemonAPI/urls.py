from django.urls import path
from . import views


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-item/<int:pk>", views.SingleMenuItemsView.as_view()),
    path("menu", views.menu),
    path("", views.welcome),
    path("secret/", views.secret),
    path("api-token-auth/", obtain_auth_token),
]
