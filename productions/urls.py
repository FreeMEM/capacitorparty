from django.urls import path
from productions import views


urlpatterns = [
    path("", views.productions, name="productions"),
    path("<int:production_id>/", views.production, name="productions"),
    path("upload", views.upload, name="upload"),
    path("author/<int:author_id>/", views.author, name="author"),
]
