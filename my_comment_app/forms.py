from django import forms
from django_comments.forms import CommentForm
from my_comment_app.models import CustomizedComment

class CustomizedCommentForm(CommentForm):
    LOCALIZATION_CHOICES = (
        ('fr','Français'),
        ('de', 'Deutsch'),
        ('en','English'),
    )
    localization = forms.ChoiceField(choices=LOCALIZATION_CHOICES)

    def get_comment_create_data(self, **kwargs):
        # Use the data of the superclass, and add in the localization field
        data = super().get_comment_create_data(**kwargs)
        data['localization'] = self.cleaned_data['localization']
        return data