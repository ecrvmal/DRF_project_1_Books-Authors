from django.urls import path, re_path
from .views import PaintersListAPIView

# this works for    http://127.0.0.1:8000/api/0.2/painters/
# urlpatterns = [
#     path('', UserListAPIView.as_view()),
# ]

# this works for  http://127.0.0.1:8000/api/0.2/painters/


app_name = 'painters'

#        for URLPathVersioning
#        there is a global urls.py, then this urls.py  is not necessary
#        this works for  http://127.0.0.1:8000/api/0.2/painters/
# urlpatterns = [
#     # re_path(r'^api/(?<version>\d.\d)/painters/$', PaintersListAPIView.as_view()),
# ]


#        for NamespaceVersioning
urlpatterns = [
    re_path('', PaintersListAPIView.as_view()),
]
