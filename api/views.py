from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

# REST Framework Modal Viewsets
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = articalSerializers
    queryset = Article.objects.all()

# REST Framework Generic Viewsets
# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin , mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class = articalSerializers
#     queryset = Article.objects.all()

# REST Framework Viewsets & Routers
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializers = articalSerializers(articles, many=True)
#         return Response(serializers.data)
    
#     def create(self, request):
#         serializer = articalSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         serializers = articalSerializers(article)
#         return Response(serializers.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = articalSerializers(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)        

#     def destroy(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# REST Generic Views & Mixins
# class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
#                     ,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = articalSerializers
#     queryset = Article.objects.all()
#     lookup_field = 'id'
    
#     # 1st it will check SessionAuthentication and then it will check BasicAuthentication
#     # like username and password
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         return self.list(request)

#     def post(self,request):
#         return self.create(request)
    
#     def put(self,request,id=None):
#         return self.update(request, id)
    
#     def delete(self, request, id):
#         return self.destroy(request, id)

# REST Class Based API Views 
# class articleView(APIView):
#     def get(self,request):
#         articles = Article.objects.all()
#         # serialize query set that's why add many=True
#         serializer = articalSerializers(articles,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = articalSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class articleDet(APIView):
#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = articalSerializers(article)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         article = self.get_object(id)
#         serializer = articalSerializers(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# REST Framework api_view() Decorators 

# @api_view(["GET","POST"])
# def article(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = articalSerializers(articles,many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = articalSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","DELETE"])
# def articleOne(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = articalSerializers(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = articalSerializers(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# # REST Framework Function Based API Views 
# @csrf_exempt
# def article(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = articalSerializers(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = articalSerializers(data=data)
#         if serializer.ipks_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=200)
#         else:
#             return JsonResponse(serializer.error,status=400)

# @csrf_exempt
# def articleOne(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = articalSerializers(article)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = articalSerializers(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#             return JsonResponse(serializer.error,status=400)
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)


