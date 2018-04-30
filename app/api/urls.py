from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewset)


urlpatterns = [

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

