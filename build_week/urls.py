from django.contrib import admin
from django.urls import path, include
from rooms import views
# from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from pusherchat.views import PusherView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('api/rooms/', views.RoomsView.as_view()),
    path('', views.RoomsView.index),
    path('api/pusher/', PusherView.broadcast)

]
