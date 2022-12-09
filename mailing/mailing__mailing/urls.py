from django.urls import path, include
from .views import (
    MailingApiView,
    MailingDetailApiView
)


urlpatterns = [
    path('', MailingApiView.as_view()),
    path('<int:mailing_id>/', MailingDetailApiView.as_view()),
]

