from rest_framework import serializers

from product.models import Products, Category, Testimonial, Updateimage


#project
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'image', 'name', 'description']


#project Details
class ProductsDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


#Category
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"



class UpdateimageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Updateimage
        fields = "__all__"