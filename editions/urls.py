from django.urls import path
from editions import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("editions", views.editions, name="editions"),
    path("editions/<int:edition_id>/", views.edition, name="edition"),
]
