from django.contrib import admin
from meetinginvite.invitations.models import InvitationBase, GiftTable, Place,ConfirmationWhatsapp

admin.site.register(InvitationBase)
admin.site.register(GiftTable)
admin.site.register(Place)
admin.site.register(ConfirmationWhatsapp)
