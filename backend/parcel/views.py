from django.db.models import Avg, Count, F, Max, Min, Q, Sum
from rest_framework import generics, views, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from backend.models import Parcel, Client, Article, ParcelQuantity
from .serializers import ParcelSerializer


class ParcelList(generics.ListAPIView):
    #queryset = Parcel.objects.all().order_by("-id")
    serializer_class = ParcelSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Parcel.objects.filter(client__created_by = user)
        if user.is_superuser:
            queryset = Parcel.objects.all().order_by("-id")
        return queryset



class ParcelCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def create(self, request):
        try:
            client = get_object_or_404(
                Client,
                id=request.data.get('client')["id"])
            if client:
                pass
            else:
                client = None
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(client=client)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED,
                                headers=headers,
                                )
        except Exception as e:
            print("Error ", e)
            print("Error data ", request.data)
            response = JsonResponse(
                {"error": "Une erreur inatendue s'est produite"})

        return response
    


class ParcelRetrieve(generics.RetrieveAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class ParcelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


@api_view(['GET', 'PUT','POST','DELETE'])
def parcels_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        parcel = Parcel.objects.get(pk=pk)
    except Parcel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParcelSerializer(parcel, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            articles = request.data.pop("articles")
            for article in articles:
                parcel.articles.add(article.get("id"))
            client = request.data.get("client")["id"]
            parcel.client = Client.objects.get(pk=client)
            serializer = ParcelSerializer(
                parcel, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print("Error ", e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        parcel.delete()
        
    elif request.method == 'POST':
        articles = request.data.pop("articles")
        for article in articles:
            parcel.articles.remove(article.get("id"))
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST'])
def update_parcel_quantity(request):
    values = {'error': '', 'has_error': 0}
    values['id_article'] = request.data.get('id_article')
    values['id_parcel'] = request.data.get('id_parcel')
    values['quantity'] = request.data.get('quantity')
    try:
        article = Article.objects.get(pk=int(values['id_article']))
        parcel = Parcel.objects.get(pk=int(values['id_parcel']))
        article_parcel = ParcelQuantity.objects.filter(
            id_article=int(values['id_article']),
            id_parcel=int(values['id_parcel']))
        if article_parcel.exists():
            detail_parcel = ParcelQuantity.objects.filter(
                id_article=article.id,
                id_parcel=parcel.id).update(
                quantity=values['quantity']
            )
        else:
            detail_parcel = ParcelQuantity.objects.create(
                id_article=article.id,
                id_parcel=parcel.id,quantity=values['quantity'])
            detail_parcel.save()
           
        return JsonResponse(values)
    except Exception as e:
        values['error'] = e
        values['has_error'] = -1
        print("erreur", e)
    return JsonResponse(values)


def get_article_quantity(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    try:
        parcel = Parcel.objects.filter(pk=parcel.id)
        parcel_quantity = ParcelQuantity.objects.filter(
            id_parcel__in=parcel)
        data = list(parcel_quantity.values())
        # anotate_parcel_quantity = parcel_quantity.annotate(Sum('id'))
        # get_parcel_quantity = anotate_parcel_quantity.aggregate(
        #     Sum('quantity'))
        return JsonResponse({"data": data})
    except Exception as e:
        print("Erreur ", e)
        data = "Une erreur s'est produite!!"
        return JsonResponse({"error": data})
