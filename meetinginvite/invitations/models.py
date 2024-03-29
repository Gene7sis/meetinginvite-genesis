from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, SlugField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.text import slugify
import uuid
from embed_video.fields import EmbedVideoField
import csv


class InvitationBase(Model):
    class Event(models.IntegerChoices):
        XV = 0, _('MIS XV')
        WEDDING = 1, _('NUESTRA BODA')
        BAPTISM = 2, _('MI BAUTIZO')
        __empty__ = _('(Pendiente)')

    slug = SlugField(_("Slug"), blank=True, max_length=255, unique=True)
    name_event = CharField(_("Nombre del evento"), blank=True, max_length=255)
    type_event = models.IntegerField(choices=Event.choices)
    date_until_event = models.DateTimeField()

    itinerary = models.ImageField(upload_to='itinerary', blank=True)
    music = models.FileField(upload_to='music', null=True, blank=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    excel_invitation = models.FileField(upload_to='excel_invitation', null=True, blank=True)
    video_url = EmbedVideoField(null=True, blank=True)
    
    
    inicio_img = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img = models.ImageField(upload_to='invitations_carrousel', blank=True)
    confirmacion_img = models.ImageField(upload_to='invitations_carrousel', blank=True)

    carrousel_img_1 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img_2 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img_3 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img_4 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img_5 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    carrousel_img_6 = models.ImageField(upload_to='invitations_carrousel', blank=True)
    
    # codigo añadido
    messages_padre = models.TextField(blank=True, null=True, verbose_name="Mensajes")
    messages_mama = models.TextField(blank=True, null=True, verbose_name="Mensajes")
    messages_padrino = models.TextField(blank=True, null=True, verbose_name="Mensajes")
    messages_otro = models.TextField(blank=True, null=True, verbose_name="Mensajes")
     # codigo añadido
     
    def __str__(self):
        return self.name_event

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(f"{self.get_type_event_display()}-{self.name_event}")
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("invitation_detail", kwargs={"slug": self.slug})


class GiftTable(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    liverpool_code = CharField(_("Liverpool"), blank=True, max_length=10)
    amazon_code = CharField(_("Amazon"), blank=True, max_length=100)
    sears_code = CharField(_("Sears"), blank=True, max_length=12)
    palacio_de_hierro_code = CharField(_("Palacio de Hierro"), blank=True, max_length=12)
    bank_name = CharField(_("Banco"), blank=True, max_length=20)
    bank_image = models.ImageField(upload_to='bank', null=True, blank=True)
    bank_account = CharField(_("Número de Cuenta"), blank=True, max_length=20)
    bank_account_name = CharField(_("Titular de la cuenta"), blank=True, max_length=255)

    def __str__(self):
        return '{}'.format(self.invitation.name_event)


class Place(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    ceremony_name = CharField(_("Nombre del lugar de la ceremonia"), blank=True, max_length=255)
    ceremony_address = CharField(_("Dirección de la ceremonia"), blank=True, max_length=255)
    ceremony_when = models.DateTimeField()
    ceremony_map = models.URLField(null=True, blank=True)
    ceremony_image = models.ImageField(upload_to='places', null=True, blank=True)
    ceremony_calendar_google = models.URLField(null=True, blank=True)
    ceremony_calendar_apple = models.FileField(upload_to='calendar', null=True, blank=True)
    ceremony_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    ceremony_lon = models.FloatField(_('Longitude'), blank=True, null=True)

    reception_name = CharField(_("Nombre del lugar de la recepción"), blank=True, max_length=255)
    reception_address = CharField(_("Dirección de la recepción"), blank=True, max_length=255)
    reception_when = models.DateTimeField()
    reception_map = models.URLField(null=True, blank=True)
    reception_image = models.ImageField(upload_to='places', blank=True)
    reception_calendar_google = models.URLField(null=True, blank=True)
    reception_calendar_apple = models.FileField(upload_to='calendar', null=True, blank=True)
    reception_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    reception_lon = models.FloatField(_('Longitude'), blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.invitation.name_event, self.ceremony_name)


class ConfirmationWhatsapp(Model):
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    name_contact = CharField(_("Nombre del contacto"), blank=True, max_length=255)
    phone_number = CharField(_("Número del contacto"), blank=True, max_length=255)
    default_message = CharField(_("Mensaje por defecto"), blank=True, max_length=999)

    def __str__(self):
        return '{}-{}-{}'.format(self.invitation.name_event, self.name_contact, self.phone_number)


def _random_uuid():
    return uuid.uuid4().hex


class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    invitation = models.ForeignKey(InvitationBase, on_delete=models.CASCADE)
    name = models.TextField()
    number_of_people = models.IntegerField(default=0)
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    observations = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    save_the_date_sent = models.DateTimeField(null=True, blank=True, default=None)
    save_the_date_opened = models.DateTimeField(null=True, blank=True, default=None)
    invitation_code = SlugField(_("Party Slug"), blank=True, max_length=255, unique=True, default=_random_uuid)
    invitation_sent = models.DateTimeField(null=True, blank=True, default=None)
    invitation_opened = models.DateTimeField(null=True, blank=True, default=None)
    is_invited = models.BooleanField(default=False)
    is_attending = models.BooleanField(default=None, null=True)
    comments = models.TextField(null=True, blank=True)
    arrived = models.BooleanField(default=None, null=True)

    def __str__(self):
        return 'Party: {}'.format(self.name)

    @classmethod
    def in_default_order(cls):
        return cls.objects.order_by('-is_invited', 'name')


def save():
    with open('invitations.csv', 'r', encoding = "ISO-8859-1") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            if row[3] == '':
                child = 0
            else:
                child = row[3]
            if row[7] == 'Digital':
                Party.objects.create(
                    invitation_id=5,
                    name=row[0],
                    number_of_people=row[1],
                    adult=row[2],
                    child=child,
                    phone_number=row[5],
                    observations=row[6],
                    comments=row[8],
                    is_invited=True
                )
            else:
                Party.objects.create(
                    invitation_id=5,
                    name=row[0],
                    number_of_people=row[1],
                    adult=row[2],
                    child=child,
                    comments=row[8],

                )

