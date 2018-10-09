from django.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


# URLs for token-based auth
urlpatterns = [
    url(r'^auth/$', obtain_jwt_token, name='user-auth'),
    url(r'^refresh/$', refresh_jwt_token, name='user-refresh'),
    url(r'^verify/$', verify_jwt_token, name='user-verify'),
]