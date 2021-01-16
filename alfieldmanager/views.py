from django.shortcuts import redirect,render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from alfieldmanager.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required,user_passes_test
from alfieldmanager.forms import ProductForm
from alfieldmanager.filters import ProductFilter 
def index(request):
    """Home page for alfield manager"""
    return render(request,'alfieldmanager/index.html')

@login_required
def products(request):
    """The product page"""

    items = Product.objects.order_by('-date_added')
    f = ProductFilter(request.GET, queryset=items)
    items = f.qs
    context = {'items':items,'filter':f
    }
  
    return render(request,'alfieldmanager/product_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'alfieldmanager/user_list.html',context)


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self,form):
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update_form'

    def form_valid(self,form):
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = '/products/'        

#def add_product(request):
#    """Add a new product"""
#    if request.method != 'Post':
#        form = ProductForm()
#    else:
#        form = ProductForm(data=request.Product)
#        if form.is_valid():
#            form.save()
#            return redirect('product')
#    context = {'form':form}
#    return render(request,'alfieldmanager/product_form.html',context)

#def edit_product(request,pk):
#    """Edit the product"""
#    product = Product.objects.get(pk=pk)
#    topic = product.topic
   
#    if request.method != 'Post':
        # Initial request; pre-fill form with the current product.
#        form = ProductForm(instance=product)
#    else:
        # Product data submitted; process data.
#        form = ProductForm(instance=product, data=request.Product)
#        if form.is_valid():
#            form.save()
#            return redirect('torains:topic', topic_id=topic.id)
#    context = {'product': product, 'topic': topic, 'form': form}
#    return render(request, 'torains/edit_product.html', context)
