from django.contrib import admin
from django.urls import path
from task1 import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('platform/', include('task1.urls')),
]
