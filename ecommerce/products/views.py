from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.

class DemoView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self ,request):
         print(request.user)
         return Response({'sucess' : "Hurray you are authenticated"})
    

class ProductAPIView(APIView):

    def get(self,request):

        category = self.request.query_params.get('category')
        print(category.capitalize())
        if category:
            queryset = Product.objects.filter(category__category_name = category.capitalize())
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset , many = True)
        if serializer.data:
            return Response({'data' :serializer.data,'count' : len(serializer.data),'message':'Data get successfully'},status=status.HTTP_200_OK)
        return Response({'data':[],'message':'Data not found'},status=status.HTTP_404_NOT_FOUND)