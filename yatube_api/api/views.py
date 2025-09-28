from rest_framework import viewsets, permissions, pagination, mixins
from rest_framework.generics import get_object_or_404

from posts.models import Post, Comment, Group, Follow

from .permissions import PostCommentPermission
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра, редактирования и удаления
    данных о публикациях
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        PostCommentPermission, permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра, редактирования и удаления
    данных о комментариях
    """

    serializer_class = CommentSerializer
    permission_classes = [PostCommentPermission, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Набор представлений для просмотра данных о группах
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Набор представлений для просмотра и создания подписок
    """

    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return user.follows.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)