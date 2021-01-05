from django.urls import path
from users import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('register/', views.registration_view, name="register"),
]