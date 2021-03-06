from django.contrib import admin

from feedback.models import ServiceFeedback


@admin.register(ServiceFeedback)
class AuthenticationFieldAdmin(admin.ModelAdmin):
    list_display = [
        'short_content', 'origin_url', 'created_on',
    ]
