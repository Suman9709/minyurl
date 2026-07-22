from django.urls import path

from core.views import LogoutUser, RegisterUser, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewset)


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout')
    
]
urlpatterns += router.urls