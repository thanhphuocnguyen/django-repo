from rest_framework import serializers
from .models import (Product, CustomerReportRecord, Cateogry, ProductSite,
                     ProductSize, Comment, Company)
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_flex_fields import FlexFieldsModelSerializer


class CompanySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Company
        fields = ('pk', 'name', 'url')


class CategorySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Cateogry
        fields = ('pk', 'name')
        expandable_fields = {
            'products': ('product_reviewer.ProductSerializer', {
                'many': True
            })
        }


class ProductSerializer(FlexFieldsModelSerializer):
    # category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'content', 'created', 'updated')
        expandable_fields = {
            'category': ('product_reviewer.CategorySerializer', {
                'many': True
            }),
            'sites': ('product_reviewer.ProductSiteSerializer', {
                'many': True
            }),
            'comments': ('product_reviewer.CommentSerializer', {
                'many': True
            }),
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductSiteSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = ProductSite
        fields = ('pk', 'name', 'price', 'url', 'created', 'updated')
        expandable_fields = {
            'product': 'product_reviewer.CateogrySerializer',
            'productsize': 'product_reviewer.ProductSizeSerializer',
            'company': 'product_reviewer.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days


class CommentSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'title', 'content', 'created', 'updated')
        expandable_fields = {
            'product': 'product_reviewer.CategorySerializer',
            'user': 'product_reviewer.UserSerializer'
        }


class CustomerReportSerializer(FlexFieldsModelSerializer):

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError('title invalid')
        return value

    class Meta:
        model = CustomerReportRecord
        fields = '__all__'