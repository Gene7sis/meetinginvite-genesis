from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, SlugField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.text import slugify


class InvitationBase(Model):
    class Event(models.IntegerChoices):
        XV = 0, _('MIS XV AÑOS')
        WEDDING = 1, _('NUESTRA BODA')
        BAPTISM = 2, _('MI BAUTIZO')
        __empty__ = _('(Pendiente)')

    slug = SlugField(_("Name of User"), blank=True, max_length=255)
    name_event = CharField(_("Nombre del evento"), blank=True, max_length=255)
    type_event = models.IntegerField(choices=Event.choices)
    date_until_event = models.DateTimeField()

    itinerary = models.ImageField(upload_to='itinerary')
    music = models.FileField(upload_to='music')
    video = models.FileField(upload_to='video')
    excel_invitation = models.FileField(upload_to='excel_invitation')
    video_url = models.URLField()

    carrousel_img_1 = models.ImageField(upload_to='invitations_carrousel')
    carrousel_img_2 = models.ImageField(upload_to='invitations_carrousel')
    carrousel_img_3 = models.ImageField(upload_to='invitations_carrousel')
    carrousel_img_4 = models.ImageField(upload_to='invitations_carrousel')
    carrousel_img_5 = models.ImageField(upload_to='invitations_carrousel')

    def __str__(self):
        return self.name_event

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify((self.name_event))
        return super().save(*args, **kwargs)


class GiftTable(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    liverpool_code = CharField(_("Liverpool"), blank=True, max_length=10)
    amazon_code = CharField(_("Amazon"), blank=True, max_length=100)
    sears_code = CharField(_("Sears"), blank=True, max_length=12)
    palacio_de_hierro_code = CharField(_("Sears"), blank=True, max_length=12)
    bank_name = CharField(_("Banco"), blank=True, max_length=12)
    bank_image = models.ImageField(upload_to='bank')
    bank_account = CharField(_("Número de Cuenta"), blank=True, max_length=12)
    bank_account_name = CharField(_("Titular de la cuenta"), blank=True, max_length=12)

    def __str__(self):
        return self.invitation

class Places(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    address_ceremony = CharField(_("Dirección"), blank=True, max_length=255)
    ceremony_when = models.DateTimeField()
    ceremony_map = models.URLField()
    ceremony_image = models.ImageField(upload_to='places')
    ceremony_calendar_google = models.URLField()
    ceremony_calendar_apple = models.FileField(upload_to='calendar')
    ceremony_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    ceremony_lon = models.FloatField(_('Longitude'), blank=True, null=True)

    reception_address = CharField(_("Dirección"), blank=True, max_length=255)
    reception_when = models.DateTimeField()
    reception_map = models.URLField()
    reception_image = models.ImageField(upload_to='places')
    reception_calendar_google = models.URLField()
    reception_calendar_apple = models.FileField(upload_to='calendar')
    reception_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    reception_lon = models.FloatField(_('Longitude'), blank=True, null=True)

    def __str__(self):
        return self.invitation

class ConfirmationWhatsapp(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    name_contact = CharField(_("Nombre del contacto"), blank=True, max_length=255)
    phone_number = CharField(_("Número del contacto"), blank=True, max_length=255)
    default_message = CharField(_("Mensaje por defecto"), blank=True, max_length=999)

    def __str__(self):
        return self.invitation
