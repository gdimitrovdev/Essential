# Django imports
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home-page"),
    path('register/', views.register, name='register'),

    path('add_todo/', views.add_todo, name="add_todo"),
    path('delete_todo/<todo_id>', views.delete_todo, name="delete_todo"),
    path('edit_todo/<path:id>', views.edit_todo, name='edit_todo'),

    path('filepost/', views.filepost, name='filepost'),
    path('deleteFile/<path:id>', views.delete_file, name='deleteFile'),

    path('add_daily_task', views.add_daily_task, name='add_daily_task'),
    path('completed/', views.completed, name='completed'),
    path('delete_task/', views.delete_task, name='delete_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
