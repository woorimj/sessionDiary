from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet

post_router = SimpleRouter(trailing_slash=True)
# 여기에 왜 / 붙을까?
post_router.register('posts', PostViewSet, basename='post')

comment_router = SimpleRouter(trailing_slash=True)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(post_router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
]