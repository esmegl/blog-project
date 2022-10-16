from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.home, name='home'),
	path('details/<int:id>/', views.details, name='details'),
	path('add-blog/', views.add_blog, name='add_blog'),
	path('edit-blog/<int:id>/', views.edit_blog, name='edit_blog'),
	path('delete-blog/<int:id>/', views.delete_blog, name='delete_blog'),
]