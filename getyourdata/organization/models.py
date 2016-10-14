from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from organization.categories import organization_categories

from getyourdata.models import BaseModel

from bs4 import BeautifulSoup, NavigableString
import re
import ptpdb


class AuthenticationField(BaseModel):
    """
    Authentication field that organizations use to identify people
    eg. email address
    """
    # The canonical name of the field (NOT TRANSLATED!)
    name = models.CharField(max_length=255, unique=True, db_index=True)

    # Name of the field displayed to the user (translatable)
    title = models.CharField(max_length=255)

    order = models.IntegerField(default=777)

    help_text = models.CharField(max_length=255, default="", blank=True)
    validator_regex = models.CharField(
        max_length=1028, default="", blank=True,
        help_text=_("If not blank, this regex is used to validate the field value"))

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title

    def required_by(self, organizations):
        return Organization.objects.filter(
            authentication_fields=self,
            id__in=organizations.values_list('id', flat=True)
        )

def form_has_fields(form, fields):
    """
    Checks if form has certain fields
    """
    for field in fields:
        if not getattr(form, field):
            return False
    return True

def validate_partial_date(value):
    """
    Validate a partial date, it can be partial, but it must yet be a valid date.
    Accepted formats are: YYYY-MM-DD, YYYY-MM, YYYY.
    2013-22 must rais a ValidationError, as 2013-13-12, or 2013-11-55.
    """
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        try:
            datetime.strptime(value, '%Y-%m')
        except ValueError:
            try:
                datetime.strptime(value, '%Y')
            except ValueError:
                raise ValidationError(u'date seems not to be correct %s' % value)

# This class is from from django-popolo
class GenericRelatable(models.Model):
    """
    An abstract class that provides the possibility of generic relations
    """
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True

# This class is from from django-popolo
class Timestampable(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = AutoCreatedField(_('creation time'))
    updated_at = AutoLastModifiedField(_('last modification time'))

    class Meta:
        abstract = True

class OrganizationDetails(Timestampable, BaseModel):
    """
    Base organization details each organization has, whether the model
    is an available organization profile or an edit draft made by an user
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"))

    # Email contact
    # TODO: handle this as special case of contact_details?
    email_address = models.EmailField(
        max_length=255,
        blank=True,
        default="",
        help_text=_("Email address used by the organization for receiving "
                    "data requests. Leave empty if the "
                    "organization only accepts requests by post."),
        verbose_name=_("Email address"))

    # Postal contact
    # TODO: handle this as special case of contact_details?
    address_line_one = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name=_("Address line 1"))
    address_line_two = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name=_("Address line 2"))
    postal_code = models.CharField(
        max_length=64,
        blank=True,
        default="",
        verbose_name=_("Postal code"))
    country = models.CharField(
        max_length=64,
        blank=True,
        default="",
        verbose_name=_("Country"))

    authentication_fields = models.ManyToManyField(
        AuthenticationField, related_name="+")

    summary = models.CharField(_("summary"), max_length=1024, blank=True, help_text=_("A one-line description of an organization"))
    description = models.TextField(_("biography"), blank=True, help_text=_("An extended description of an organization"))

    data_processing_description = models.TextField(_("nature_of_work"), blank=True, help_text=_("A description of how data controller processes personal data"))
    freedom_of_information_flag = models.BooleanField(
        default=False,
        verbose_name=_("Yes"),
        help_text=_("Whether organisation has duty to respond to Freedom of Information requests"))

    partial_date_validator = RegexValidator(regex="^[0-9]{4}(-[0-9]{2}){0,2}$", message="Date has wrong format")
    dpa_registration_start_date = models.CharField(
        _("start date"), max_length=10, blank=True, null=True,
        validators=[partial_date_validator, validate_partial_date],
        help_text=_("The date when the validity of the item starts"),
    )
    dpa_registration_end_date = models.CharField(
        _("end date"), max_length=10, blank=True, null=True,
        validators=[partial_date_validator, validate_partial_date],
        help_text=_("The date when the validity of the item ends")
    )

    # array of items referencing "http://popoloproject.com/schemas/other_name.json#"
    other_names = GenericRelation('OtherName', help_text="Alternate or former names")

    # array of items referencing "http://popoloproject.com/schemas/identifier.json#"
    identifiers = GenericRelation('Identifier', help_text="Issued identifiers")
    # classification = models.CharField(_("classification"), max_length=512, blank=True, help_text=_("An organization category, e.g. committee"))
    classification = GenericRelation('Classification', help_text="Organization's classification accoring to some schema")
    tags = models.CharField(_("tags"), max_length=512, blank=True, help_text=_("Tags that reflect e.g. the organization's type"))

    # array of items referencing "http://popoloproject.com/schemas/link.json#"
    links = GenericRelation('Link', help_text="URLs to documents about the organization")

    # array of items referencing "http://popoloproject.com/schemas/link.json#"
    sources = GenericRelation('Source', help_text="URLs to source documents about the organizat    ion")

    # django-popolos definition of area class seems excessive, so just using a string for now
    jurisdiction =  models.CharField(_("area"), max_length=1024, blank=True, default="United Kingdom", help_text=_("Jurisdiction that organisation is registered in"))

    # Quick way of doing categories, let's do this properly with classes when
    # we know what exactly our needs are when tagging organisations.
    def classifications_with_links(self):
        """ Parse the organization's tags and return a dict with plaintext names and links to categories. """
        tags = self.tags.split(' ')
        categories = []
        for tag in tags:
            if tag in organization_categories:
                categories.append({'category_name': organization_categories[tag]['organisation_type_singular'],
                    'category_link': reverse('organization:list_organizations', kwargs={'tag':tag})})
        return categories

    # So far this only works for data from ICO's Register
    def data_processing_description_plaintext(self):
        """ Returns description of processing in plaintext """
        def is_header(text):
            """ Is it a header in ICO's output? """
            HEADERS = [
                'Reasons/purposes for processing information',
                'Type/classes of information processed',
                'We also process sensitive classes of information that may include:',
                'Who the information is processed about',
                'We process personal information about:',
                'Who the information may be shared with',
                'Where necessary or required we share information with:',
                'Transfers'
                ]
            return text in HEADERS

        def get_text(tag):
            if isinstance(tag, basestring):
                text = tag
            else:
                text = tag.text
            return text

        desc = self.data_processing_description
        soup = BeautifulSoup(desc, 'html.parser')
        # Collect output in array
        output = []
        # iterate through top-level tags
        for tag in soup.children:
            text = get_text(tag)
            # remove leading and trailing whitespace
            text = text.strip()
            # skip if only whitespace
            if not text or text.isspace(): continue
            # skip first few descriptive tags from ICO
            if 'Nature of work -' in text: continue
            if 'The following is a broad description of the' in text: continue
            if 'Description of processing' in text: continue
            # note the lists inside UL tags
            if tag.name == 'ul':
                # remove all tags except <li>
                text = re.sub('(?i)<(?!li).*?>', '', str(tag))
                items = text.split('<li>')[1:]
                # lead with * for ist items
                output.extend(list('* ' + s for s in items))
            else:
                # lead with # for headers
                if is_header(text): text = '# ' + text
                output.append(text)
        return output

    def data_processing_description_displayed(self):
        """ The part of data processing description displayed by default """
        desc = self.data_processing_description_plaintext()
        # find the index of the second row that starts with '#' (where second header starts)
        second_header = next(idx for idx in range(1,len(desc)) if desc[idx][:1] == '#')
        return desc[0:second_header]

    def data_processing_description_collapsed(self):
        """ The part of data processing description collapsed by default """
        desc = self.data_processing_description_plaintext()
        # find the index of the second row that starts with '#' (where second header starts)
        second_header = next(idx for idx in range(1,len(desc)) if desc[idx][:1] == '#')
        return desc[second_header:]

    def plaintext_description(self):
        """ Return organisation description without potential HTML tags and []-style references
        """
        desc = re.sub('<[^<]+?>', '', self.description)
        desc = re.sub('\[[^\[]+?\]', '', desc)
        return desc

    class Meta:
        abstract = True

    def clean(self):
        postal_address_requirements = [
            "address_line_one",
            "postal_code",
            "country"
        ]
        if not (form_has_fields(self, ["email_address"]) or
                form_has_fields(self, postal_address_requirements)):
            raise ValidationError(
                _("Organization profile must contain either a valid email "
                  "address or postal information"))
        return self


class Organization(OrganizationDetails):
    """
    Organization that is accessible to all users
    """
    # Has admin verified this organization as having correct information
    verified = models.BooleanField(
        default=False,
        verbose_name=_("Verified"),
        help_text=_("Verified organizations are visible to all users"))

    requested_amount = models.IntegerField(default=0)

    class Meta:
        ordering = ('-requested_amount', 'name')

    @property
    def has_description(self):
        return self.description != ""

    @property
    def has_classification(self):
        return self.classification != ""

    @property
    def has_data_processing_description(self):
        return self.data_processing_description != ""

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
        return self.registers(manager='objects').all().exists()

    @property
    def has_comments(self):
        return self.comments(manager='objects').all().exists()

    @property
    def average_rating(self):
        rating = self.comments(manager='objects').all().aggregate(
            avg=Avg('rating'))['avg']

        if rating:
            return format(float(rating), '.1f')
        return '0'

    @property
    def amount_ratings(self):
        return self.comments(manager='objects').all().count()

    def __unicode__(self):
        return self.name


class Register(BaseModel):
    """
    Organization may have multiple registers
    """
    # name of the register
    name = models.CharField(
        max_length=255,
        help_text=_("The name of the register used by the organization. "
                    "Eg. Customer register"),
        verbose_name=_("Name of the person register"))
# which organization this register belongs to
    organization = models.ForeignKey(
        Organization,
        related_name='registers',
        on_delete=models.CASCADE
    )
    help_text = models.CharField(max_length=255, default="", blank=True)

    def __unicode__(self):
        return self.name


class OrganizationDraft(OrganizationDetails):
    """
    Organization draft created when an user modifies an existing organization
    and submits the suggestions. Only visible to the site staff.
    """
    class Meta:
        verbose_name = "organization edit draft"
        verbose_name_plural = "organization edit drafts"
        ordering = ('updated_on',)

        permissions = (
            ("check_organization_draft",
                _("Can check organization drafts and update the original "
                  "organization")),
        )

    original_organization = models.ForeignKey(
        "organization.Organization", related_name="original_organizations")

    checked = models.BooleanField(default=False)
    ignored = models.BooleanField(default=False)
    updated = models.BooleanField(default=False)


class Comment(BaseModel):
    """
    Public comment posted on an organization profile
    """
    organization = models.ForeignKey(Organization, related_name='comments')
    message = models.TextField(max_length=2000)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )

    class Meta:
        ordering = ('-created_on',)

    def __unicode__(self):
        return 'Comment ' + unicode(self.organization)

class OtherName(GenericRelatable, models.Model):
    """
    An alternate or former name
    see schema at http://popoloproject.com/schemas/name-component.json#
    """
    name = models.CharField(_("name"), max_length=512, help_text=_("An alternate or former name"))
    note = models.CharField(_("note"), max_length=1024, blank=True, help_text=_("A note, e.g. 'Birth name'"))

    def __str__(self):
        return self.name

class Identifier(GenericRelatable, models.Model):
    """
    An issued identifier
    see schema at http://popoloproject.com/schemas/identifier.json#
    """
    identifier = models.CharField(_("identifier"), max_length=512, help_text=_("An issued identifier, e.g. a DUNS number"))
    scheme = models.CharField(_("scheme"), max_length=128, blank=True, help_text=_("An identifier scheme, e.g. DUNS"))

    def __str__(self):
        return "{0}: {1}".format(self.scheme, self.identifier)

class Classification(GenericRelatable, models.Model):
    classification = models.CharField(_("classification"), max_length=512, help_text=_("A classification for this Organization within some classification scheme"))
    scheme = models.CharField(_("scheme"), max_length=128, blank=True, help_text=_("A classification scheme, e.g. SIC"))

    def __str__(self):
        return "{0}: {1}".format(self.scheme, self.classification)

class Link(GenericRelatable, models.Model):
    """
    A URL
    see schema at http://popoloproject.com/schemas/link.json#
    """
    url = models.URLField(_("url"), max_length=350, help_text=_("A URL"))
    note = models.CharField(_("note"), max_length=512, blank=True, help_text=_("A note, e.g. 'Wikipedia page'"))

    def __str__(self):
        return self.url

class Source(GenericRelatable, models.Model):
    """
    A URL for referring to sources of information
    see schema at http://popoloproject.com/schemas/link.json#
    """
    url = models.URLField(_("url"), help_text=_("A URL"))
    note = models.CharField(_("note"), max_length=512, blank=True, help_text=_("A note, e.g. 'Parliament website'"))

    def __str__(self):
        return self.url

