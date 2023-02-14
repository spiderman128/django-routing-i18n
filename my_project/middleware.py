from django.conf import settings
from django.utils import translation
from django_six import MiddlewareMixin
import os

class MultiDomainMiddleware(MiddlewareMixin):
    def process_request(self, request):
        translator = request.get_host().split(".")[0]
        if(self.checkTranslator(translator)):
            os.environ['LOCALIZATION'] = translator
        else:
            os.environ['LOCALIZATION'] = 'en'
        translation.activate(os.environ['LOCALIZATION'])
        print('Language selected ... ' + os.environ['LOCALIZATION'])
        return

    def checkTranslator(self, trans):
        languages = settings.LANGUAGES
        flg = False
        for item in languages:
            if trans in item:
                flg = True
                break
            else:
                continue
        return flg
