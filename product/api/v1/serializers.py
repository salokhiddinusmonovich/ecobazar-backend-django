from rest_framework import serializers
from product.models import Product, Feedback, Images
from category.models import Color, Category, StockStatus, Tag, Type
from user.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'image', 'name']


class ProductSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['pk', 'title', 'price', 'discount', 'main_image']


    def get_main_image(self, obj):
        main_image = obj.images_set.first()
        if main_image and main_image.image:
            return main_image.image.url
        return "No image"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['pk', 'image']





class FeedbackListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    class Meta:
        model = Feedback
        fields = ['id',  'star', 'body', 'products', 'author']




class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['star', 'body', 'products']


class FeedbackUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['body', 'star']

class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']



class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryNameSerializer(read_only=True)
    images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['pk', 'title', 'description', 'price', 'discount', 'category', 'type', 'stock_status', 'comments', 'images']

    def get_images(self, obj):
        images = Images.objects.filter(product=obj)
        serializer = ImageSerializer(images, many=True)
        return serializer.data

    def get_comments(self, obj):
        feedback = Feedback.objects.filter(products=obj)
        serializer = FeedbackListSerializer(feedback, many=True)
        return serializer.data


