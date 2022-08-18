from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehicle_repairs import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'blogposts', views.BlogPostViewSet, basename="blogpost")
router.register(r'vehicles', views.VehicleViewSet, basename="vehicle")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
