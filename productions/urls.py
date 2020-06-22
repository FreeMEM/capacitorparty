from django.urls import path
from productions import views


urlpatterns = [
    # path('list/', productionlist, name="productionlist"),
    # path('production/', production, name="production"),
    path('', views.productions, name='productions'),
]