from django.urls import path, include
from users.views import *

urlpatterns =[ path('', profile ,name='profile'),
              path('edit/', profile_edit, name='profile_edit'),
              path('onboarding/', profile_edit, name='onboarding'),
              path('chat', include('chat.urls'))
]