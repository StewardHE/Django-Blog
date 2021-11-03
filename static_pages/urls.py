from django.urls import path

from .views import home_view # home_view is the funcion that return to the archive html 

app_name = 'static_pages'

# Note: the path is the route of the web
urlpatterns = [
    path('home', home_view, name='home'),
]
