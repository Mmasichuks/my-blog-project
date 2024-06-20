from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
      path('product', views.product, name='product'),
       path('contact', views.contact, name='contact'),
        path('about', views.about, name='about'),
         path('blog', views.blog, name='blog'),
]