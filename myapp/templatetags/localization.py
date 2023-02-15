from django import template
import os
register = template.Library()

@register.filter
def localization_title(obj):
    match os.environ['LOCALIZATION']:
        case 'de':
            if (obj.title_de.strip() == ''):
                return obj.title
            return obj.title_de
        case 'fr':
            if (obj.title_fr.strip() == ''):
                return obj.title
            return obj.title_fr
        case _:
            return obj.title

@register.filter    
def localization_text(obj):
    match os.environ['LOCALIZATION']:
        case 'de':
            if (obj.text_de.strip() == ''):
                return obj.text
            return obj.text_de
        case 'fr':
            if (obj.text_fr.strip() == ''):
                return obj.text
            return obj.text_fr
        case _:
            return obj.text