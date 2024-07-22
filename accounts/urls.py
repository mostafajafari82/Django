from django.urls import path
from accounts.views import LoginView ,LogoutView, SingUpView


urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('signup/', SingUpView, name='singup'),
]
