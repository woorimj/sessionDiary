from django.shortcuts import render

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 댓글 작성자 가져오기
    # def perform_create(self, serializer):
    #     serializer.save(writer = self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # 댓글 작성자 가져오기
    # def perform_create(self, serializer):
    #     serializer.save(writer = self.request.user)

    # Override
    def get_queryset(self, **kwargs):
        id = self.kwargs['post_id']
        return self.queryset.filter(post=id)