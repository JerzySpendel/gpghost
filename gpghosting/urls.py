from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','main.views.index'),
    url(r'^index$','main.views.index'),
    url(r'^login$','main.views.login'),
    url(r'^register$','main.views.register'),
    url(r'^main$','main.views.main'),
    url(r'^main/manage/$','main.views.manage'),
    url(r'^main/managef/$','main.views.managef'),
    url(r'^main/logout/$','main.views.logout')
)
