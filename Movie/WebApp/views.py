from django.shortcuts import render
from WebApp.models import Movie
from django.http import JsonResponse
from WebApp.serializers import MovieSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

class Movie_listAV(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Movie_detailsAV(APIView):
    def get(self,request,pk):
        try:
            movies=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Not found'},status=status.HTTP_404_NOT_FOUND)


        serializer=MovieSerializer(movies)
        return Response(serializer.data)

    def put(self,request,pk):
        movies=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movies=Movie.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

    

        

# @api_view(['GET','POST'])
# def Movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def Movie_details(request,pk):
#     if request.method=='GET':
#         movies=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movies)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         movies=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors

#     if request.method=='DELETE':
#         movies=Movie.objects.get(pk=pk)
#         movies.delete()

    

# Create your views here.
# def Movie_list(request):
#     movies=Movie.objects.all()
#     #print(movies.values())
#     data={'movies':list(movies.values())}
#     return JsonResponse(data)
    
# def Movie_details(request,pk):
#     movies=Movie.objects.get(pk=pk)
#     data={
#         'name':movies.name,
#         'description':movies.description,
#         'active':movies.active,
#     }
#     return JsonResponse(data)