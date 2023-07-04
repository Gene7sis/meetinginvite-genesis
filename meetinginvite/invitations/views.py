from django.shortcuts import render
from django.views.generic import TemplateView
from meetinginvite.invitations.models import InvitationBase, Party
from django.views.generic import ListView, DetailView
from datetime import datetime
import re

def cambiar_fondo(request):
    return render(request, 'base.html')

class AboutView(TemplateView):
    template_name = "invitation_base.html"

class InvitationDetailView(DetailView):
    model = InvitationBase
    template_name = "invitation_template.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()


        return context
    


class InvitationCodeDetailView(DetailView):
    model = Party
    template_name = "invitation_party_template.html"
    slug_url_kwarg = 'invitation_code'


    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        invitation_code = self.kwargs.get('invitation_code')

        return Party.objects.get(invitation_code=invitation_code, invitation__slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        
         # Accessing the GET query parameters
        param1 = self.request.GET.get('colorTexto')
        
        if(param1 == "blanco"):
            color = "text-white"
        else:
            color = "text-black"
            
        # Add the parameters to the context
        context['colorText'] = color
    
        print(param1)
        print(color)
        
        return context
    





# def invitation(request, invite_id):
#     party = guess_party_by_invite_id_or_404(invite_id)
#     if party.invitation_opened is None:
#         # update if this is the first time the invitation was opened
#         party.invitation_opened = datetime.utcnow()
#         party.save()
#     if request.method == 'POST':
#         for response in _parse_invite_params(request.POST):
#             guest = Guest.objects.get(pk=response.guest_pk)
#             assert guest.party == party
#             guest.is_attending = response.is_attending
#             guest.meal = response.meal
#             guest.save()
#         if request.POST.get('comments'):
#             comments = request.POST.get('comments')
#             party.comments = comments if not party.comments else '{}; {}'.format(party.comments, comments)
#         party.is_attending = party.any_guests_attending
#         party.save()
#         return HttpResponseRedirect(reverse('rsvp-confirm', args=[invite_id]))
#     return render(request, template_name='guests/invitation.html', context={
#         'party': party,
#         'meals': MEALS,
#     })
