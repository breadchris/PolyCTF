import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram.settings")
django.setup()

from app.models import Post, Comment, InstagramUser

user = InstagramUser.objects.create_superuser("christhompson", "christhompson@gmail.com", "password")

user.is_admin = True
user.save()

