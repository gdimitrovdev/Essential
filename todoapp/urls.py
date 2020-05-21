from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
	path('',views.home,name="home-page"),
	path('add/',views.add,name="add"),
	path('delete/<todo_id>', views.delete, name="delete"),
	path('register/',views.register,name='register'),
	path('edit/<path:id>', views.edit, name='edit'),
	path('filepost/', views.filepost, name='filepost'),
	path('deleteFile/<path:id>', views.deleteFile, name='deleteFile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)