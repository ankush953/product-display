from django.urls import path, include
from product import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('<int:id>',views.detail,name='detail'),
]