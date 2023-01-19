from django.contrib import admin
from meetinginvite.invitations.models import InvitationBase, GiftTable, Places,ConfirmationWhatsapp

admin.site.register(InvitationBase)
admin.site.register(GiftTable)
admin.site.register(Places)
admin.site.register(ConfirmationWhatsapp)
