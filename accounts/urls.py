from django.urls import path 

from .views import(
    user_create_view,
    user_login_view,
    user_logout_view,
    user_profile_view
)
# app name
app_name = 'accounts'

urlpatterns = [
    path('create/', user_create_view, name = "create"),
    path('login/', user_login_view, name = "login"),
    path('logout/', user_logout_view, name = "logout"),
    path('<str:username>/', user_profile_view, name = "profile")
]
