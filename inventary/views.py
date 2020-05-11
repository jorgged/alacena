from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
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
        return reverse_lazy('inventary:DetailProduct',kwargs={'pk': product_id})


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
    context_object_name="group"
    template_name = "group/DetailGroup.html"


class ShoppingCartListView(ListView):
    model = ShoppingCartModel
    context_object_name="products"
    template_name = "shoppingcart/ListShopping.html"

class ShoppingCartCreateView(CreateView):
    model = ShoppingCartModel
    template_name = "shoppingcart/CreateShopping.html"
    success_url = reverse_lazy('inventary:ListShopping')



def ShoppingCartView(request, pk):
    if pk is not None:
        product = ProductModel.objects.get(id=pk)
        product.InList = True
        product.save()
        return HttpResponse("ok")
    return HttpResponseBadRequest("bad")
