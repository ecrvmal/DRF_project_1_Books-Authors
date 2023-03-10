from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter, SimpleRouter  # this helps to define entry points
from users.views import UserModelViewSet
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet
from painters.views import PaintersListAPIView, PaintersViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'users'
# app_name = 'painters'


router = DefaultRouter()  # initiate the class

# register entry point to model
# entry point = users , that we had imported
router.register('users', UserModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
router.register('painters', PaintersViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to our project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # permissions for documentation view
    permission_classes=[permissions.AllowAny],
)

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

    # below is for URLPathVersioning   this works for  http://127.0.0.1:8000/api/0.2/users/
    # this works for    http://127.0.0.1:8000/api/0.2/users/
    # re_path(r'^api/(?P<version>\d\.\d)/painters/$', PaintersListAPIView.as_view()),

    # below is for NamespaceVersioning   this works for  http://127.0.0.1:8000/api/0.2/users/
    # path('api/painters/0.1', include('painters.urls', namespace='0.1')),
    # path('api/painters/0.2', include('painters.urls', namespace='0.2')),

    # Versioning in URL address
    # defined in routers
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
