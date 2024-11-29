from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login, name='login'),
    path('logout/', views.LOGOUT, name='logout'),
    path('post/<int:ID>', views.post, name='post'),
    path('register/', views.signup, name='register'),
    path('', views.homepage, name='home'),
    path('user/', include('User.urls')),
    path('post/', include('post.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
