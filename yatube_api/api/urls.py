from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowAPIView


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowAPIView, basename='follow')

urlpatterns = [
    path('', include('djoser.urls.jwt')),
]

urlpatterns += router.urls