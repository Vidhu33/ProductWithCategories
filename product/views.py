from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError

from .models import Category,SubCategory,Product
from .serializers import CategorySerializer,SubCategorySerializer,ProductSerializer


class CategoryHandler(APIView):
    def __init__(self):
        self.queryset = Category.objects.all()
        self.filter_backends = (DjangoFilterBackend,)

    def get(self,request,pk=None):
        serializer = CategorySerializer(self.queryset,many=True)
        return Response({"CategoryList":serializer.data})


class SubCategoryHandler(APIView):
    def __init__(self):
        self.queryset = SubCategory.objects.all()
        self.filter_backends = (DjangoFilterBackend,)
        self.filter_fields = ('id','category__category_name','sub_category_name')

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self,request):
        queryset = self.filter_queryset(self.queryset)
        serializer = SubCategorySerializer(queryset,many=True)
        return Response({"results":serializer.data})

class ProductHandler(APIView):
    def __init__(self):
        self.queryset = Product.objects.all()
        self.filter_backends = (DjangoFilterBackend,)
        self.filter_fields = ('id','sub_category__sub_category_name','product_name',)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self,request):
        category_name = request.GET.get("category")
        if category_name:
            category = Category.objects.filter(category_name=category_name)
            if category:
                queryset = self.queryset.filter(sub_category__category=category[0])
        else:
            queryset = self.filter_queryset(self.queryset)
        serializer = ProductSerializer(queryset,many=True)
        return Response({"results":serializer.data})

    def post(self,request):
        data = self.request.data
        try:
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                result = serializer.save(serializer.validated_data)
                return Response({"results":ProductSerializer(result).data})
            else:
                raise(ValidationError(serializer.errors))
        except ValidationError as err:
            content = {"errors":err.messages}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response("Internal Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    