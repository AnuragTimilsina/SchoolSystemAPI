from rest_framework.routers import DefaultRouter
from api.views import AssignmentViewSet

router = DefaultRouter()
router.register(r'', AssignmentViewSet)

urlpatterns = router.urls