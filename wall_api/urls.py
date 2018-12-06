from django.urls import path
from rest_framework.routers import DefaultRouter

from wall_api.views import MessageViewSet,register



urlpatterns = [
    path('register/',register)
]

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
urlpatterns += router.urls