from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView,\
    GroupCreateView, GroupListView, GroupUpdateView, ProductDetailView, GroupDetailView, \
    ShoppingCartListView, AddToShoppingCart, QuitToShoppingCart


app_name = "inventary"
urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name="CreateProduct"),
    path('', ProductListView.as_view(), name="ListProduct"),
    path('product/update/<int:pk>/',
         ProductUpdateView.as_view(), name="UpdateProduct"),
    path('Product/<int:pk>/', ProductDetailView.as_view(), name="DetailProduct"),


    path('group/create/', GroupCreateView.as_view(), name="CreateGroup"),
    path('group/update/<int:pk>/', GroupUpdateView.as_view(), name="UpdateGroup"),
    path('group/list/', GroupListView.as_view(), name="ListGroup"),
    path('group/<int:pk>/', GroupDetailView.as_view(), name="DetailGroup"),

    # urls del shoppingcart
    path('shoppingcart/add/<int:pk>/', AddToShoppingCart, name="AddToShoppingCart"),
    path('shoppingcart/delete/<int:pk>/', QuitToShoppingCart, name="QuitShoppingCart"),
    path('shoppingcart/List/',ShoppingCartListView.as_view(), name="ListShopping"),


]
