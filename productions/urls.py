from django.urls import path
from productions import views


urlpatterns = [
    path('', views.productions, name='productions'),
    path('upload', views.upload, name='upload'),
]