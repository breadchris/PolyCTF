from django.conf import settings
# Essentially creates MEDIA_URL as a global variable in templates
def media_url(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL
    }

