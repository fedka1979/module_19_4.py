from django.urls import path
from task1.views import shop, cart, home
from .views import sign_up_by_django, sign_up_by_html


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path("", sign_up_by_html, name="html_sign_up"),
    path("django_sign_up/", sign_up_by_django, name="django_sign_up"),
]