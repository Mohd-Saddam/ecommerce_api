from django.urls import path

from .views import ProductAPIView,DemoView

urlpatterns = [
    path('products/',ProductAPIView.as_view()),
    path('demo/' , DemoView.as_view()),

  
]