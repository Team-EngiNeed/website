from django.urls import path
from . import views

app_name = 'engineed'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('researchers', views.researchers, name='researchers'),
    path('index_new', views.index_new, name='index_new'),
    path('page', views.page, name='page'),
    path('adviser', views.adviser, name='adviser'),
    path('engineer', views.engineer, name='engineer'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]


