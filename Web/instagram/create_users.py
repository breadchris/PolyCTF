import json, datetime, os, shutil, ntpath, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram.settings")
django.setup()

from app.models import InstagramUser
from django.core.files import File

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

users_file = open('FakeNameGenerator.com_2e7f203f.csv', 'r')
users_csv = csv.reader(users_file)

for user in users_csv:
    if len(InstagramUser.objects.filter(username=user[1])) > 0:
        print "User: %s already exists" % user[1]
        break
        
    db_user = InstagramUser(username=user[1], email=user[2])

    db_user.name = user[0]

    '''
    picture_path = 'profile_pictures/%s' % path_leaf(user['profile_picture']) 
    
    try:
        shutil.copyfile(user['profile_picture'], 'instagram/media/' + picture_path)
    except IOError, e:
        print "Copying picture failed. %s" % e

    profile_picture = open('instagram/media/' + picture_path, 'r')

    db_user.profile_picture.save(picture_path, File(profile_picture))
    '''
    db_user.profile_picture.save('media/pictures/profile_pictures/default.png', File(open('/home/christopher/Documents/Coding/instagram-clone/instagram/instagram/media/profile_pictures/default.png')))

    db_user.save()
    print "[+] Created User: %s" % user[1]

users_file.close()

