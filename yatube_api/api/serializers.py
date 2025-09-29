from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    # Решил в сериализаторе сделать) тут как-то удобнее
    def validate(self, attrs):
        user = self.context['request'].user
        following = attrs.get('following')
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписываться на самого себя'
            )
        follow = Follow.objects.filter(user=user, following=following)
        if follow.exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя'
            )

        return attrs

    class Meta:
        fields = ('user', 'following')
        model = Follow
