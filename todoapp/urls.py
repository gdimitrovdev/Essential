from django.urls import path
from . import views 

urlpatterns=[
	path('',views.home,name="home-page"),
	path('add/',views.add,name="add"),
	path('delete/<todo_id>', views.delete, name="delete"),
	path('register/',views.register,name='register')
]