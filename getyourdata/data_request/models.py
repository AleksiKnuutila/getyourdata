from __future__ import unicode_literals

from django.db import models

from organization.models import Organization, AuthenticationField


class DataRequest(models.Model):
    organization = models.ForeignKey(Organization, related_name="data_requests")

    def __unicode__(self):
        return "Data request for " + self.organization.name


class AuthenticationContent(models.Model):
    auth_field = models.ForeignKey(AuthenticationField, related_name="+")
    data_request = models.ForeignKey(DataRequest, related_name="auth_contents")
    content = models.CharField(max_length=255)

    def __unicode__(self):
        return "Authentication content"