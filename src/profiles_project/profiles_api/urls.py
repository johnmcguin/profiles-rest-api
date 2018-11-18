from django.conf.urls import url
from django.conf.urls import include

# used to route to API View SEts
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    # no url because it's the default router
    url(r'', include(router.urls))
]