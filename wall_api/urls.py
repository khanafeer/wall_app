from django.urls import path
from rest_framework.routers import DefaultRouter

from wall_api.views import MessageView,register



urlpatterns = [
    path('register/',register),
    path('messages/',MessageView.as_view())
]
