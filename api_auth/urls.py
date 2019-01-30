from django.urls import path
from .views import Login, Logout

urlpatterns = [
    path('login/', Login.as_view(), name="auth-login"),
    path('logout/', Logout.as_view(), name="auth-logout"),
]