from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter, SimpleRouter  # this helps to define entry points
from users.views import UserModelViewSet
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet
from userapp.views import UserListAPIView

app_name = 'users'
# app_name = 'userapp'

urlpattern = []

router = DefaultRouter()  # initiate the class

# register entry point to model
# entry point = users , that we had imported
router.register('users', UserModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)

# for lesson 9
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # connect  path = api/    router
    path('api-token-auth/', views.obtain_auth_token),  # for Token auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # for JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # for JWT
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),

]
