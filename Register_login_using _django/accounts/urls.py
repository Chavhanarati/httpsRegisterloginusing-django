from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
from django.urls import path


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(),name='login'),
    path('api/logout/', knox_views.LogoutViews.as_view(),name='logout'),
    path('api/logoutall/', knox_views.LogoutViews.as_view(),name='logoutall'),
]
