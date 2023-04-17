from django.urls import path, include
from .views import (
   NewsList, NewDetail, SearchNewsList, AddNew, UpdateNew, DeleteNew)



urlpatterns = [
   path('', NewsList.as_view(),
name='news'),
   path('<int:pk>', NewDetail.as_view(),
name='new'),
   path('search/', SearchNewsList.as_view(),
name='news_search'),
   path('add/', AddNew.as_view(),
name='new_add'),
   path('update/<int:pk>', UpdateNew.as_view(),
name='new_update'),
   path('delete/<int:pk>', DeleteNew.as_view(),
name='new_delete'),
]