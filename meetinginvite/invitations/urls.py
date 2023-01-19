from django.urls import path

from meetinginvite.invitations.views import (
    AboutView,
)

app_name = "invitations"
urlpatterns = [
     path('home/', AboutView.as_view()),
]
