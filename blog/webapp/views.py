from django.shortcuts import render
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


# Register your models here.
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    ###client_class = OAuth2Client###

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# Create your views here.
