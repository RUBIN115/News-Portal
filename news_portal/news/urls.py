from django.urls import path, include
from .views import NewsList, NewDetail



urlpatterns = [
   # path('', ProductsList.as_view()),
   # path('<int:pk>', ProductDetail.as_view()),
   path('', NewsList.as_view()),
   path('<int:pk>', NewDetail.as_view()),
]