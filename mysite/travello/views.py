from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination
from rest_framework import viewsets
from .serializers import DestSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
 
 # Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

def index(request):
    
    
    dests= Destination.objects.all()

    return render(request,'index.html',{'dests':dests})


# Create your views here.
class DestViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all().order_by('name')
    serializer_class = DestSerializer