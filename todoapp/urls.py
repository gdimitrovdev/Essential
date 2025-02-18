# Django imports
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('register/', views.register, name='register'),

    path('add_todo/', views.add_todo, name="add_todo"),
    path('delete_todo/', views.delete_todo, name="delete_todo"),
    path('complete_todo/', views.complete_todo, name="complete_todo"),
    path('edit_todo/<path:id>', views.edit_todo, name='edit_todo'),

    path('filepost/', views.filepost, name='filepost'),
    path('deleteFile/<path:id>', views.delete_file, name='deleteFile'),

    path('add_daily_task', views.add_daily_task, name='add_daily_task'),
    path('completed/', views.completed, name='completed'),
    path('delete_task/', views.delete_task, name='delete_task'),

    # a path to download a file
    path('download/<path:file_id>', views.download, name='download')
]
