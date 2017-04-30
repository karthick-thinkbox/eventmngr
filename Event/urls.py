from django.conf.urls import url
from .views import user_reg,managerview,table,addevent,exitpage
from django import forms
from .forms import userform
from .preview import userformPreview

urlpatterns = [
    
       url(r'register/$',user_reg,name='register_page'), 
       url(r'manage/$',managerview,name='manager_page'),
       url(r'cat/(?P<pk>.*)/$', table,name='table_page'),
       url(r'addevent/$',addevent,name='newevt_page'),
       url(r'logout/$',exitpage,name='logout_page'),
       url(r'^post/$', userformPreview(userform)),
   
    ]