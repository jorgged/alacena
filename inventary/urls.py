from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView,GroupCreateView,GroupListView, GroupUpdateView


app_name = "inventary"
urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name="CreateProduct"),
    path('list/', ProductListView.as_view(), name="ListProduct"),
    path('product/update/<int:pk>/',ProductUpdateView.as_view(), name="UpdateProduct"),
    path('group/create/', GroupCreateView.as_view(),name="CreateGroup"),
    path('group/update/<int:pk>/',GroupUpdateView.as_view(),name="UpdateGroup"),
    path('group/list/',GroupListView.as_view(),name="ListGroup"),

]