from rest_framework import serializers
from organization.models import Organization, Register, Comment, OtherName, Identifier, Classification, Link, Source

# future expansion to support multiple registers per organization
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'name')


# future expansion to enable displaying of all ratings/comments on organization list page
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('rating', 'message')

class OtherNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherName
        fields = ('name', 'note')

class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = ('identifier', 'scheme')

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('classification', 'scheme')

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('url', 'note')

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('url', 'note')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):

    registers = serializers.StringRelatedField(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    other_names = OtherNamesSerializer(many=True, read_only=True)
    identifiers = IdentifierSerializer(many=True, read_only=True)
    classification = ClassificationSerializer(many=True, read_only=True)
    links = LinkSerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'verified',
            'accepts_email',
            'accepts_mail',
            'address_line_one',
            'address_line_two',
            'postal_code',
            'country',
            'email_address',
            'registers',
            'average_rating',
            'amount_ratings',
            'tags',
            'comments',
            'summary',
            'description',
            'jurisdiction',
            'data_processing_description',
            'freedom_of_information_flag',
            'dpa_registration_start_date',
            'dpa_registration_end_date',
            'other_names',
            'identifiers',
            'classification',
            'links',
            'sources'
        )
        depth = 2
