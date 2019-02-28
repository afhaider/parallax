from django.urls import path,include
from . import views

from rest_framework import routers
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router=routers.DefaultRouter()
router.register( 'users', UserViewSet)
router.register('Comment',views.CommentView)

urlpatterns = [
    path('',views.indexf,name='Adminpanel-indexf'),
    path('futurepost',views.viewsf,name='Adminpanel-viewsf'),
    path('zero/',include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
   
]
