from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',

    url(
        r'^/$', 
        views.workplaces, 
        name='workplaces'
    ),


# Business ##########################################################


    url(
        r'^/workplace/$', 
        views.WorkplaceList.as_view(), 
        name='workplace-list'
    ),
    url(
        r'^/workplace/(?P<pk>[0-9]+)/$', 
        views.WorkplaceDetail.as_view(), 
        name='workplace-detail'
    ),

)

urlpatterns = format_suffix_patterns(urlpatterns)