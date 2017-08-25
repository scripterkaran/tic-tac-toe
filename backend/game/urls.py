from rest_framework import routers
from .viewsets import *


router = routers.SimpleRouter()
router.register(r'tic-tac-toe', TicTacToeViewSet)


urlpatterns = router.urls