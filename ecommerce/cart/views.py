from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CartItemSerializer, OrderSerializer

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItem.objects.filter(cart = cart)
        serializer= CartItemSerializer(queryset,many=True)

        print(user)
        return Response({"message":"It's working","data":serializer.data})

    def post(self,request):
        user = request.user
        data = request.data
        cart,_ = Cart.objects.get_or_create(user  = user,ordered = False)
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_item = CartItem(cart = cart, user = user, product = product, price = price, quantity = quantity)
        cart_item.save()

        total_price=0
        cart__items = CartItem.objects.filter(user = user, cart = cart.id)
        for items in cart__items:
            total_price +=items.price
        cart.total_price = total_price
        cart.save()

        return Response({"message":"Item added to your cart"})

    def put(self,request):
        data = request.data

        cart_item = CartItem.objects.get(id = data.get('id'))
        quantity = int(data.get('quantity'))

        cart_item.quantity += quantity
        cart_item.save()

        return Response({"message":"Item updated"})

    def delete(self,request):
        
        user = request.user
        data = request.data
        cart_item  = CartItem.objects.get(id = data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItem.objects.filter(cart = cart)
        serializer= CartItemSerializer(queryset,many=True)

        print(user)
        return Response({"message":"It's working","data":serializer.data})
    

class OrderAPI(APIView):

    def get(self,request):
        queryset   = Order.objects.filter(user = request.user)
        serializer = OrderSerializer(queryset,many = True)

        return Response(serializer.data)

    