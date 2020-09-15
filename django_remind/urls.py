from django.contrib import admin
from django.urls import path, include
from viewcrud.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('viewcrud/', include('viewcrud.urls')),
]
