from rest_framework import routers
from .viewsets import *
from rest_framework_nested import routers as nested_routers


router = routers.SimpleRouter()
router.register(r'game', GameViewSet)

nested_router = nested_routers.NestedSimpleRouter(router, r'game', lookup='game')
nested_router.register(r'moves', MoveViewSet, base_name='move')

urlpatterns = router.urls

urlpatterns += urlpatterns + (nested_router.urls)