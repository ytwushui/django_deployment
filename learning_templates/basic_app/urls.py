from django.conf.urls import url,include
from basic_app import views

# template tagging
# look up the basic app and find the urls matches
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'^other/$',views.other, name = 'other'),
    url(r'^register/$',views.register, name = 'register'),
    url(r'^user_login/$',views.user_login, name='user_login')
]
