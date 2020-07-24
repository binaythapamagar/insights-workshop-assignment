from django.urls import path
from django.urls.conf import include
from .views import dashboard,registration


urlpatterns = [
    path('dashboard',dashboard,name='users_dashboard'),
    path('register',registration,name='register'),
    path('accounts/',include('django.contrib.auth.urls'))
]