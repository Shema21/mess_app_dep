from django.contrib import admin
from django.urls import path, include
from chats import auth 
from rest_framework.routers import DefaultRouter
from chats.views import ConversationViewSet, MessageViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')), 
    
    # JWT endpoints
    path('api/token/', auth.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', auth.TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]





