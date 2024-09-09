
from django.contrib import admin
from django.urls import path, include
from home.views import *
from chat.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', home, name='home'),
path('accounts/', include('allauth.urls')),
path('profile', include('users.urls')),
path('chats', chats, name='chats'),
path("__reload__/", include("django_browser_reload.urls")),
]
