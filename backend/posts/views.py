from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer

# Create your views here.





class PostViewSet(viewsets.ModelViewSet): # new   پبشرفته تر
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ModelViewSet): # new     پبشرفته تر
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer