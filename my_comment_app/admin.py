from django_comments.admin import CommentsAdmin
from django.contrib import admin
from .models import CustomizedComment
from django.utils.translation import gettext_lazy as _

class CustomCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {'fields': ('content_type', 'object_pk', 'site')}
        ),
        (
            _('Content'),
            {'fields': ('user', 'user_name', 'user_email', 'user_url', 'comment', 'localization')}
        ),
        (
            _('Metadata'),
            {'fields': ('submit_date', 'ip_address', 'is_public', 'is_removed')}
        ),
    )
    list_display = ('name', 'content_type', 'object_pk', 'localization', 'ip_address', 'submit_date', 'is_public', 'is_removed')

admin.site.register(CustomizedComment, CustomCommentAdmin)