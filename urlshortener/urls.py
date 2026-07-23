
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from urlshortener import views
from urlshortener.views import CreateLink, LinkViewset  

router = DefaultRouter()
router.register(r'api/shorten-link', LinkViewset, basename='link')
urlpatterns = [
  path("links/", CreateLink.as_view()),
   path('links/<str:short_code>/', views.RedirectViewset.as_view(), name='redirect-link'),
]
urlpatterns += router.urls
