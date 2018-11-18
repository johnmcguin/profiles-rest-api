from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete',
            'Similar to traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk stands for primary key (id for object in db)
    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Updates only fields provides in the request."""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method:', 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'a_viewset': a_viewset})

    def create(self, request):
        """Creates new objects in the system."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieves a specific object by id."""

        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Updates an object by id"""

        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles a partial update to an object by id"""

        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles the deletion of a particular object by id."""
        
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles createing, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # token auth
    authentication_classes = (TokenAuthentication,)
    # permissions
    permission_classes = (permissions.UpdateOwnProfile,)
    # filters
    filter_backends = (filters.SearchFilter,)
    # fields to filter by (search by)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer
    
    def create(self, request):
        """User the ObtainAuthToken to validate and create a token."""

        return ObtainAuthToken().post(request)