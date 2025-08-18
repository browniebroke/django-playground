from rest_framework.viewsets import ModelViewSet
from playground.apps.blog.models import Post
from playground.apps.blog.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer