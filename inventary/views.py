from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import ProductModel, GroupProductModel, ShoppingCartModel
from .forms import ProductForm,GroupProductForm


class ProductCreateView(CreateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/CreateProduct.html"


class ProductListView(ListView):
    model = ProductModel
    context_object_name = "products"
    template_name = "product/ListProduct.html"


class ProductUpdateView(UpdateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/UpdateProduct.html"


class GroupCreateView(CreateView):
    model = GroupProductModel
    form_class= GroupProductForm
    template_name = "group/CreateGroup.html"

class GroupUpdateView(UpdateView):
    model = GroupProductModel
    form_class= GroupProductForm
    template_name = "group/UpdateGroup.html"

class GroupListView(ListView):
    model = GroupProductModel
    context_object_name ="groups"
    template_name = "group/ListGroup.html"



def ShoppingCartView(request, pk):
    if pk is not None:
        product = ProductModel.objects.get(id=pk)
        product.InList = True
        product.save()
        return HttpResponse("ok")
    return HttpResponseBadRequest("bad")
