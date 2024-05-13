from django.contrib import admin

from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["commenter", "content", "response_to"],
            },
        ),
        (
            "Additional options",
            {
                "classes": ["collapse"],
                "fields": ["creation_date", "up_votes"],
            },
        ),
    ]