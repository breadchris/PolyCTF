import os, hashlib
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

# Model helper methods
def get_profile_image_path(instance, filename):
    return os.path.join('profile_pictures', filename)

def get_post_image_path(instance, filename):
    return os.path.join('post_pictures', filename)

class InstagramUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = InstagramUserManager.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = email,
            username = username,
            password = password
        )

        user.is_admin = True
        user.save(using=self.db)
        return user

class InstagramUser(AbstractBaseUser):
    # Allow Instagram user to extend base User Model
    email = models.CharField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=1024)
    profile_picture = models.ImageField(upload_to=get_profile_image_path, default='profile_pictures/default_user_picture.png')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = [email]
    USERNAME_FIELD = 'username'

    objects = InstagramUserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        super(InstagramUser, self).save(*args, **kwargs)

class Post(models.Model):
    description = models.CharField(max_length=255)
    creation_date = models.DateField()
    user = models.ForeignKey(InstagramUser, related_name="posts")
    picture = models.FileField(upload_to=get_post_image_path)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.description

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    creation_date = models.DateField()
    user = models.ForeignKey(InstagramUser)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "%s commented on %s's post" % (self.user.name, self.post.user.name)

class Follower(models.Model):
    follower = models.ForeignKey(InstagramUser, related_name="followers")
    user = models.ForeignKey(InstagramUser, related_name="following")

    def __unicode__(self):
        return "%s if following %s" % (self.follower.username, self.user.username)

class Like(models.Model):
    user = models.ForeignKey(InstagramUser)
    post = models.ForeignKey(Post, related_name="likes")

