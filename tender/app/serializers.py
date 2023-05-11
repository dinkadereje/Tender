from rest_framework.serializers import ModelSerializer
from app.models import Category, Region, Tender, Company, DocumentBid


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class TenderSerializer(ModelSerializer):

    class Meta:
        model = Tender
        fields = '__all__'


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class DocumentBidSerializer(ModelSerializer):

    class Meta:
        model = DocumentBid
        fields = '__all__'
