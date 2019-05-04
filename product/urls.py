from django.urls import path, include
from product import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('product/<int:id>',views.detail,name='detail'),
    path('email/<int:id>',views.email,name='email'),
]