from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "invitation_base.html"