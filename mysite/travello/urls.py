from django.urls import include,path
from . import views
from rest_framework import routers
from .views import RegisterAPI

router = routers.DefaultRouter()
router.register(r'Destinations', views.DestViewSet)


urlpatterns= [
    path("", views.index, name="index"),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]

