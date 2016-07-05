from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from getyourdata.models import BaseModel


class AuthenticationField(BaseModel):
    # The canonical name of the field (NOT TRANSLATED!)
    name = models.CharField(max_length=255, unique=True, db_index=True)

    # Name of the field displayed to the user (translatable)
    title = models.CharField(max_length=255)

    help_text = models.CharField(max_length=255, default="", blank=True)
    validator_regex = models.CharField(
        max_length=1028, default="", blank=True,
        help_text=_("If not blank, this regex is used to validate the field value"))

    def __unicode__(self):
        return self.title


class Organization(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"))

    # Email contact
    email_address = models.EmailField(
        max_length=255, null=True, blank=True,
        default="",
        help_text=_("Email address used by the organization to respond to user data requests"),
        verbose_name=_("Email address"))

    # Postal contact
    address_line_one = models.CharField(
        max_length=255, null=True, blank=True,
        default="",
        verbose_name=_("Address line 1"))
    address_line_two = models.CharField(
        max_length=255, null=True, blank=True,
        default="",
        verbose_name=_("Address line 2"))
    postal_code = models.CharField(
        max_length=64, null=True, blank=True,
        default="",
        verbose_name=_("Postal code"))
    country = models.CharField(
        max_length=64, null=True, blank=True,
        default="",
        verbose_name=_("Country"))

    # Has admin verified this organization as having correct information
    verified = models.BooleanField(
        default=False,
        verbose_name=_("Verified"),
        help_text=_("Verified organizations are visible to all users"))

    authentication_fields = models.ManyToManyField(
        AuthenticationField, related_name="+")

    class Meta:
        ordering = ('created_on',)

    @property
    def accepts_email(self):
        return self.email_address != ""

    @property
    def accepts_mail(self):
        return self.address_line_one != "" and \
               self.postal_code != "" and \
               self.country != ""

    @property
    def has_registers(self):
        return self.register_set is not None


    def __unicode__(self):
        return self.name


class Register(BaseModel):

    # name of the register
    name = models.CharField(max_length=255,
                            help_text=_("The name of the register used by the organization. Eg. Customer register"),
                            verbose_name=_("Name of the person register"))

    # which organization this register belongs to
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    help_text = models.CharField(max_length=255, default="", blank=True)

    def __unicode__(self):
        return self.name