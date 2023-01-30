from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets, status, filters
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCatView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        products = self.queryset.all()
        try:
            category = request.GET.get('category')
            if int(category) != 0:
                cat = Category.objects.filter(id=category).all()
                products = self.queryset.filter(category__id=category).all()
                page = int(request.GET.get('page'))
                prds = products[:(page * 8 + 1)]
                serializer = self.get_serializer(prds, many=True)
                return Response(serializer.data)
            else:
                page = int(request.GET.get('page'))
                # products = Product.objects.all()
                prds = products[:(page * 8 + 1)]
                serializer = self.get_serializer(prds, many=True)
                return Response(serializer.data)
        except:
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
            
            
                       
class AddLike(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        prd_id = kwargs['pk']
        product = self.queryset.filter(id=prd_id).first()
        product.likes += 1
        all = 0
        product.save()
        for i in self.queryset:
            all += i.likes
        if (100 * product.likes) / all >= 5:
            product.top = True
        product.save()
        
        return Response({"Status Okk"}, status=status.HTTP_200_OK)


class DeleteLike(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        prd_id = kwargs['pk']
        product = self.queryset.filter(id=prd_id).first()
        product.likes -= 1
        product.save()
        all = 0
        for i in self.queryset:
            all += i.likes
        if (100 * product.likes) / all <= 5:
            product.top = False
        product.save()

        return Response({"Status Okk"}, status=status.HTTP_200_OK)


class BestProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = self.queryset.all().order_by("-likes")
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class NationalityView(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class TopProductView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(top=True).all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = self.queryset.all()
        try:
            page = int(request.GET.get('page'))
            prds = products[:(page * 8 + 1)]
            serializer = self.get_serializer(prds, many=True)
            return Response(serializer.data)
        except:
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
            

class ProductSearchView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(top=True).all()
    serializer_class = ProductSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name_uz", "name_en", "name_ru", "name_ma", "name_sw"]
