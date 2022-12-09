from django.urls import path, include
from .views import (
    MessageApiView,
    MessageDetailApiView
)


urlpatterns = [
    path('', MessageApiView.as_view()),
    path('<int:message_id>/', MessageDetailApiView.as_view()),
]

