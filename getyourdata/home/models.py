from __future__ import unicode_literals

from django.db import models

from tinymce import models as tinymce_models

from getyourdata.models import BaseModel


class HomePage(BaseModel):
    admin_name = models.CharField(max_length=30, default='home', unique=True)
    content = tinymce_models.HTMLField(blank=True, default='')

    def __unicode__(self):
        return self.admin_name
