# myapy/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'friends', views.FriendViewSet)
router.register(r'belonging', views.BelongingViewSet)
router.register(r'borrowed', views.BorrowedViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URL's for the browsable API
urlpatterns = [
    path('', include(router.urls)), # primeira página do local host (padrão é não botar nada mas posso botar qualquer coisa)
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]

