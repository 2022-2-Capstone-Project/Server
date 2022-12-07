"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from user.views import *
from tour_theme.views import *
from tour.views import *
from tour_application.views import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'tour-themes', TourThemeViewSet)
router.register(r'sign-up', JWTProfileSignUpView)
router.register(r'permission', PermissionViewSet)
router.register(r'tours', TourViewSet)
router.register(r'tour-applications', TourApplicationViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API Document",
      default_version='v1',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('my-tour-themes/', MyTourThemeList.as_view()),
    path('my-tours/', MyTourList.as_view()),
    path('token/', JwtTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('user_info/<str:username>/', ProfileDetailView.as_view()),
    path('tour-theme/search', SearchTourTheme.as_view()),
    path('tour/search', SearchTour.as_view()),
    path('tour/start/<int:pk>', StartTour.as_view()),
    path('tour/end/<int:pk>', EndTour.as_view()),
    path('tour-applications/add/<int:tour_id>', AddParticipant.as_view()),
    path('my-application/', ApplicationTourList.as_view()),
    path('tour/earn-point/<int:tour_id>', EarnPoint.as_view()),
    # path('tour-themes/',  include('tour_theme.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

