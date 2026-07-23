from django.urls import path

from core.views import LogoutUser, ProfileView, RegisterUser, UserViewset
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'users', UserViewset)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutUser.as_view(), name='logout')
    
]
urlpatterns += router.urls