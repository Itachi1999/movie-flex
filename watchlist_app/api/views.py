from watchlist_app.models import DigitalContent, StreamingPlatform
from watchlist_app.api.serializers import DigitalContentSerializer, StreamingPlatformSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class StreamingPlatformList(APIView):
    def get(self, request, format=None):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StreamingPlatformSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StreamingPlatformDetail(APIView):
    def get_object(self, id):
        try:
            return StreamingPlatform.objects.get(id=id)
        except StreamingPlatform.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        platform = self.get_object(id)
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        platform = self.get_object(id)
        serializer = StreamingPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        platform = self.get_object(id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DigitalContentListAV(APIView):
    def get(self, request, format=None):
        movies = DigitalContent.objects.all()
        serializer = DigitalContentSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DigitalContentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DigitalContentDetailAV(APIView):
    def get_object(self, id):
        try:
            return DigitalContent.objects.get(id=id)
        except DigitalContent.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = DigitalContentSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = DigitalContentSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = DigitalContent.objects.all()
#         serializer = DigitalContentSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = DigitalContentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     try:
#         movie = DigitalContent.objects.get(id=id)
#     except DigitalContent.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = DigitalContentSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = DigitalContentSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)