
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls') ), 
    
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), 
    # /login/ (POST)
    # /logout/ (POST)
    # /password/reset/ (POST)
    # /password/reset/confirm/ (POST)
    # /user/ (GET, PUT, PATCH)
    
    # path('api/v1/dj-rest-auth/registration/',
    #     include('dj_rest_auth.registration.urls')),  # اضافه کردن URLهای ثبت‌نام
    # /registration/ (POST) - New user signup
    # /verify-email/ (POST) - Email verification
    
    # path('api/v1/dj-rest-auth/jwt/',
    #     include('dj_rest_auth.jwt_auth.urls')),
    
    
    
]
