from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, jwt_token,
                    user_register)

v1_router = DefaultRouter()
v1_router.register(
    r'titles',
    TitleViewSet,
    basename='titles'
)
v1_router.register(
    r'genres',
    GenreViewSet,
    basename='genres'
)
v1_router.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(r'users', UserViewSet, basename='users')

auth_urlpatterns = [
    path('signup/', user_register, name='register'),
    path('token/', jwt_token, name='token')
]
v1_urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include(auth_urlpatterns))
]
