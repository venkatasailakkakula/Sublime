from django.urls import path
from RestApp import views
urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name='ab'),
	path('cnt/',views.contact,name='cn'),
	path('lgn/',views.login,name='lg'),
]