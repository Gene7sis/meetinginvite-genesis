from django.urls import path

from meetinginvite.invitations.views import (
    AboutView, InvitationDetailView, InvitationCodeDetailView
)

app_name = "invitations"
urlpatterns = [
    path("<slug:slug>", InvitationDetailView.as_view(), name="invitation_detail"),
    path("<slug:slug>/<slug:invitation_code>/", InvitationCodeDetailView.as_view(), name="invitation_party_detail"),
    path('home/', AboutView.as_view()),

]
