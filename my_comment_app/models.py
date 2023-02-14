from django.db import models
from django_comments.abstracts import CommentAbstractModel

class CustomizedComment(CommentAbstractModel):
    LOCALIZATION_CHOICES = (
        ('fr','Français'),
        ('de', 'Deutsch'),
        ('en','English'),
    )

    localization = models.CharField(
        max_length=10,
        choices=LOCALIZATION_CHOICES,
        default='en',
    )