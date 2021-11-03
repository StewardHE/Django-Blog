from django.urls import path

# import all views of the archive views.py
from .views import (
    post_create_view,
    post_detail_view,
    post_list_view,
    post_update_view,
    post_delete_view
)

# App name
app_name = 'posts'

# urls 
urlpatterns = [
    path('create/', post_create_view, name='create'),
    path('detail/<int:id>', post_detail_view, name='detail'),
    path('list/', post_list_view, name='list'),
    path('update/<int:id>', post_update_view, name='update'),
    path('delete/<int:id>', post_delete_view, name='delete')
]