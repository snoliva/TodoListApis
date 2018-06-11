from django.urls import path
from django.conf.urls import url
from .views import UserCreateApiView, UserLoginApiView, ListTaskApiView, UpdateStatusApiView

app_name = 'api/users'

urlpatterns = [
   url(r'register/$', UserCreateApiView.as_view(), name='register'),
   url(r'login/$', UserLoginApiView.as_view(), name='login'),
   url(r'list/$', ListTaskApiView.as_view(), name='listtask'),
   url(r'edit/(?P<id>[0-9]+)$', UpdateStatusApiView.as_view(), name='update'),
]