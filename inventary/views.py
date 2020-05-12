from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest
from .models import ProductModel, GroupProductModel, ShoppingCartModel
from .forms import ProductForm, GroupProductForm


class ProductCreateView(CreateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/CreateProduct.html"
    success_url = reverse_lazy('inventary:ListProduct')


class ProductListView(ListView):
    model = ProductModel
    context_object_name = "products"
    template_name = "product/ListProduct.html"


class ProductDetailView(DetailView):
    model = ProductModel
    context_object_name = "product"
    template_name = "product/DetailProduct.html"


class ProductUpdateView(UpdateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/UpdateProduct.html"

    def get_success_url(self):
        product_id = self.kwargs['pk']
        return reverse_lazy('inventary:DetailProduct', kwargs={'pk': product_id})


class GroupCreateView(CreateView):
    model = GroupProductModel
    form_class = GroupProductForm
    template_name = "group/CreateGroup.html"
    success_url = reverse_lazy('inventary:ListGroup')


class GroupUpdateView(UpdateView):
    model = GroupProductModel
    form_class = GroupProductForm
    template_name = "group/UpdateGroup.html"

    def get_success_url(self):
        group_id = self.kwargs['pk']
        return reverse_lazy('inventary:DetailGroup', kwargs={'pk': group_id})


class GroupListView(ListView):
    model = GroupProductModel
    context_object_name = "groups"
    template_name = "group/ListGroup.html"


class GroupDetailView(DetailView):
    model = GroupProductModel
    context_object_name = "group"
    template_name = "group/DetailGroup.html"


class ShoppingCartListView(ListView):
    model = ShoppingCartModel
    context_object_name = "items"
    template_name = "shoppingcart/ShoppingCart.html"
    

def AddToShoppingCart(request, pk):
    product_id = pk
    if product_id is not '':
        try:
            product = ProductModel.objects.get(pk=product_id)
        except ProductModel.DoesNotExist:
            return HttpResponseBadRequest(content="el producto no existe")
        ShoppingCart = ShoppingCartModel()
        ShoppingCart.Product = product
        ShoppingCart.Check = False
        ShoppingCart.save()
        HttpResponse(status=201)
    else:
        return HttpResponseBadRequest('no se pudo agregar al carrito')

def QuitToShoppingCart(request, pk):
    item_id = pk
    if item_id is not '':
        # import ipdb; ipdb.set_trace()
        try:
            item = ShoppingCartModel.objects.get(pk=item_id)
        except ShoppingCartModel.DoesNotExist:
            return HttpResponseBadRequest(content="el item seleccionado no existe")
        item.delete()
        return HttpResponse(status=201)
    else:
        return HttpResponseBadRequest(content="ocurrio un error en quitar el item del carrito")