from rest_framework import routers
from .viewsets import *


router = routers.SimpleRouter()
router.register(r'tic-tac-toe', TicTacToeViewSet)
router.register(r'tic-tac-toe-move', TicTacToeMoveViewSet)

urlpatterns = router.urls