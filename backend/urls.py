from django.urls import path
from .parcel.views import (
    ParcelList,
    ParcelRetrieveUpdateDestroy,
    ParcelCreate,
    ParcelRetrieve,
    parcels_detail,
    update_parcel_quantity,
    get_article_quantity
)
from .article.views import (
    ArticleList,
    ArticleRetrieveUpdateDestroy,
    ArticleCreate,
    ArticleRetrieve
)
from .client.views import (
    ClientList,
    ClientRetrieveUpdateDestroy,
    ClientCreate,
    ClientRetrieve
)
from .delivery.views import (
    DeliveryList,
    DeliveryRetrieveUpdateDestroy,
    DeliveryCreate,
    DeliveryRetrieve,
    delivery_detail
)
urlpatterns = [
    # Parcel urls
    path('parcel/', ParcelList.as_view()),
    path('parcel/detail/<int:pk>/', ParcelRetrieve.as_view()),
    path('parcel/create/', ParcelCreate.as_view()),
    path('parcel/delete/<int:pk>/', ParcelRetrieveUpdateDestroy.as_view()),
    path('parcel/update/<int:pk>/', parcels_detail),
    path('parcel/update_parcel_quantity/', update_parcel_quantity),
    path('parcel/get_article_quantity/<int:parcel_id>/', get_article_quantity),
    # Article urls
    path('article/', ArticleList.as_view()),
    path('article/detail/<int:pk>/', ArticleRetrieve.as_view()),
    path('article/create/', ArticleCreate.as_view()),
    path('article/update/<int:pk>/', ArticleRetrieveUpdateDestroy.as_view()),
    # Client urls
    path('client/', ClientList.as_view()),
    path('client/detail/<int:pk>/', ClientRetrieve.as_view()),
    path('client/create/', ClientCreate.as_view()),
    path('client/update/<int:pk>/', ClientRetrieveUpdateDestroy.as_view()),
    # Delivery urls
    path('delivery/', DeliveryList.as_view()),
    path('delivery/detail/<int:pk>/', DeliveryRetrieve.as_view()),
    path('delivery/create/', DeliveryCreate.as_view()),
    path('delivery/update/<int:pk>/',delivery_detail),
    path('delivery/delete/<int:pk>/', DeliveryRetrieveUpdateDestroy.as_view()),
]
