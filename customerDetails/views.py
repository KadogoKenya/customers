from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Business,LocationDetails
from .serializer import BusinessSerializer,LocationSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound


# Create your views here.


class BusinessAPI(APIView):
    def get(self, request, format=None):
        business = Business.objects.all()
        serializers = BusinessSerializer(business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        # appointments = self.get_object(pk)
        books = BusinessSerializer.filter(pk = pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)