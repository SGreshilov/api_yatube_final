from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register()

urlpatterns = [
]

urlpatterns += router.urls
