from django.urls import path 
from .views import ItemDeleteView

urlpatterns = [
       path('items/delete/<int:item_id>/', ItemDeleteView.as_view(), name='item-delete'),
]