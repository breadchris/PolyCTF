from django.conf import settings
from app.models import InstagramUser
from django.views.generic import ListView
from django.conf.urls import patterns, url, include
from app.views import IndexView, RegisterView, LoginView, LogoutView, AccountView, AccountSearch, PostView

urlpatterns = patterns('',
    (r'^/?$', IndexView.as_view()),
    (r'^register/?$', RegisterView.as_view()),
    (r'^login/?$', LoginView.as_view()),
    (r'^logout/?$', LogoutView.as_view()),
    (r'^posts/view/(?P<pk>[-_\w]+)/?$', PostView.as_view()),
    (r'^accounts/(?P<slug>[-_\w]+)/?$', AccountView.as_view()),
    (r'^search/(?P<query>\w+)/$', AccountSearch.as_view()),
    (r'^search/$', AccountSearch.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )


