from django.shortcuts import render
from.models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
def indexf(request):
	comments=Comment.objects.all()
	context={'comments':comments,'title': 'Announcements'}
	return render(request,"Adminpanel/adpanel.html", context)

def viewsf(request):
	comments=Comment.objects.all()
	context={'comments':comments,'title': 'FuturePosts'}
	return render(request,"Adminpanel/FuturePosts.html", context)

class CommentView(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer