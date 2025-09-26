from rest_framework import viewsets

from posts.models import Post, Comment, Group
from .serializers import PostSerializer, CommentSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра, редактирования и удаления
    данных о публикациях
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра, редактирования и удаления
    данных о комментариях
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Набор представлений для просмотра данных о группах
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer