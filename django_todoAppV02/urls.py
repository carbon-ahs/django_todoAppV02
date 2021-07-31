from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin', admin.site.urls),
	path('', include('polls_app.urls')),
	#path('', include('t_app.urls')),
]