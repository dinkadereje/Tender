from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers import CategorySerializer, RegionSerializer, TenderSerializer, CompanySerializer, DocumentBidSerializer
from app.models import Category, Region, Tender, Company, DocumentBid


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RegionViewSet(ViewSet):

    def list(self, request):
        queryset = Region.objects.order_by('pk')
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Region.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RegionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response(status=404)
        serializer = RegionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TenderViewSet(ViewSet):

    def list(self, request):
        queryset = Tender.objects.order_by('pk')
        serializer = TenderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Tender.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = TenderSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Tender.objects.get(pk=pk)
        except Tender.DoesNotExist:
            return Response(status=404)
        serializer = TenderSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Tender.objects.get(pk=pk)
        except Tender.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CompanyViewSet(ViewSet):

    def list(self, request):
        queryset = Company.objects.order_by('pk')
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response(status=404)
        serializer = CompanySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DocumentBidViewSet(ViewSet):

    def list(self, request):
        queryset = DocumentBid.objects.order_by('pk')
        serializer = DocumentBidSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DocumentBidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DocumentBid.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DocumentBidSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = DocumentBid.objects.get(pk=pk)
        except DocumentBid.DoesNotExist:
            return Response(status=404)
        serializer = DocumentBidSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = DocumentBid.objects.get(pk=pk)
        except DocumentBid.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
