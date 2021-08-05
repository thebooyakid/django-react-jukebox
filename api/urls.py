from django.urls import path
from django.urls.conf import include
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
]