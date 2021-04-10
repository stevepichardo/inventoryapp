from django.urls import path
from . import views

app_name = 'ItemForm'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('newitem', views.create_item, name='create_item'),
    path('update/<str:pk>', views.update_item, name='update_item'),
    path('delete/<str:pk>', views.delete_item, name='delete_item')
]