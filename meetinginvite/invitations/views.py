from django.shortcuts import render
from django.views.generic import TemplateView
from meetinginvite.invitations.models import InvitationBase
from django.views.generic import ListView, DetailView
from datetime import datetime
class AboutView(TemplateView):
    template_name = "invitation_base.html"

class InvitationDetailView(DetailView):
    model = InvitationBase
    template_name = "invitation_template.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
