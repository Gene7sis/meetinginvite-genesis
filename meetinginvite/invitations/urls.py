from django.urls import path

from meetinginvite.invitations.views import (
    AboutView, InvitationDetailView
)

app_name = "invitations"
urlpatterns = [
    path("<slug:slug>", InvitationDetailView.as_view(), name="invitation_detail"),
    # path("<slug:slug>", InvitationDetailView.as_view(), name="invitation_detail"),  # new
    path('home/', AboutView.as_view()),
]
