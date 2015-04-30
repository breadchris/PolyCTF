import json, datetime, os, shutil, ntpath, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram.settings")

django.setup()

from app.models import Post, Comment, InstagramUser, Like
from django.core.files import File

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

posts_file = open('posts.json', 'r')
posts_json = json.load(posts_file)
posts = posts_json['posts']

for post in posts:
    post_user = InstagramUser.objects.filter(username=post['user'])[0]

    print post_user

    db_post = Post(description=post['description'], creation_date=datetime.datetime.now(), user=post_user, picture=None)

    picture_path = 'post_pictures/%s' % path_leaf(post['picture'])
    
    post_picture = open('instagram/media/' + picture_path, 'r')

    db_post.picture.save(picture_path, File(post_picture))

    db_post.save()

    likes = post['likes']
    for like in likes:
        db_like = Like()
        db_like.user = InstagramUser.objects.filter(username=like)[0]
        db_like.post = db_post
        db_like.save()

    comments = post['comments']
    for comment in comments:
        comment_user = InstagramUser.objects.filter(username=comment['user'])[0]
        db_comment = Comment()
        db_comment.comment = comment['comment']
        db_comment.creation_date = datetime.datetime.now()
        db_comment.user = comment_user
        db_comment.post = db_post
        db_comment.save()

posts_file.close()

