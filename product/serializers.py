from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Category,SubCategory,Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name")

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    sub_category_name = serializers.CharField(source="sub_category.sub_category_name")
    category_name = serializers.CharField(source="sub_category.category.category_name")

    class Meta:
        model = Product
        fields = '__all__'

    def validate_category_name(self,category_name):
        try:
            category = Category.objects.get(category_name=category_name)
            return category
        except:
            raise ValidationError("Category Not Found")

    def validate_sub_category_name(self,sub_category_name):
        try:
            sub_category = SubCategory.objects.get(sub_category_name=sub_category_name)
            return sub_category
        except:
            raise ValidationError("SubCategory Not Found")

    def save(self, validated_data):
        prod_obj = Product()
        prod_obj.product_name = validated_data.get("product_name")
        prod_obj.sub_category = validated_data.get('sub_category')['sub_category_name']
        prod_obj.save()
        return prod_obj