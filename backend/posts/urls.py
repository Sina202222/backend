# posts/urls.py

# from django.urls import path
from .views import  UserViewSet, PostViewSet
    

from rest_framework.routers import SimpleRouter



router = SimpleRouter()   # new   پبشرفته تر
router.register('users', UserViewSet, basename='users')   # new   پبشرفته تر
router.register('', PostViewSet, basename='posts')   # new   پبشرفته تر
   
urlpatterns = router.urls   # new   پبشرفته تر