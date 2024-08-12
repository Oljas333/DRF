from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from News.views import CategotyApiView, CommentApi, ArtiLesApi, search

router = routers.DefaultRouter()
router.register(r'api/cat', CategotyApiView)
router.register(r'api/art', ArtiLesApi)
router.register(r'api/com', CommentApi)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('News/', include('News.urls')),
    path('', include(router.urls)),
]
