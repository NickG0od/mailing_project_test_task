from django.urls import path, include
from .views import (
    ClientApiView,
    ClientDetailApiView
)


urlpatterns = [
    path('', ClientApiView.as_view()),
    path('<int:client_id>/', ClientDetailApiView.as_view()),
]

