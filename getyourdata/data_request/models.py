from __future__ import unicode_literals

from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone

from getyourdata.models import BaseModel
from data_request.services import convert_html_to_pdf
from organization.models import Organization, AuthenticationField

class PdfContents(BaseModel):
    title  = models.CharField(max_length=255, default="Default", unique=True)
    header = models.CharField(max_length=255, blank=True, default="Dear recipient,")
    content1 = models.TextField(blank=True, default="content eka")
    content2 = models.TextField(blank=True, default="content toka")
    footer = models.CharField(max_length=255, blank=True, default="Regards,")
    class Meta:
        verbose_name_plural="pdf contents"

class AuthenticationContent(BaseModel):
    # We don't actually want to save these...
    auth_field = models.ForeignKey(AuthenticationField, related_name="+")
    data_request = models.ForeignKey("data_request.DataRequest", related_name="auth_contents")
    content = models.CharField(max_length=255)

    def __unicode__(self):
        return "Authentication content"

class DataRequest(BaseModel):
    organization = models.ForeignKey(Organization, related_name="data_requests")

    def to_html(self):
        """
        Return data request as a HTML-formatted document
        """
        try:
            person_name = self.auth_contents.get(auth_field__name="name")
        except:
            person_name = None

        pdfcontent, created = PdfContents.objects.get_or_create(title="Default")
        return render_to_string(
            "data_request/mail/request.html", {"data_request": self,
                                               "person_name": person_name,
                                               "pdfcontent": pdfcontent,
                                               "current_datetime": timezone.now()})

    def to_pdf(self):
        """
        Return data request as a PDF-formatted document
        """
        return convert_html_to_pdf(self.to_html())

    def __unicode__(self):
        return "Data request for " + self.organization.name
