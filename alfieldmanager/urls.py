from . import views
from .views import ProductCreateView,ProductUpdateView,ProductDeleteView
from django.urls import include,path

urlpatterns = [
   path('',views.index,name='index'),
   path('products/',views.products,name='product'),
   path('add-product/',ProductCreateView.as_view(),name='add_product'),
   path('administrator/',views.users,name='administrator'),
   path('products/<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
   path('products/<int:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
]
