from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from playground.apps.blog.models import Post
from playground.apps.blog.serializers import PostSerializer


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 2


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"
    pagination_class = SmallPageNumberPagination
