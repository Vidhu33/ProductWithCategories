from django.urls import path
from .views import *

urlpatterns = [
    # url to home page
    path('category/',CategoryHandler.as_view()),
    path('category/<str:pk>/',CategoryHandler.as_view()),
    path('sub_category/',SubCategoryHandler.as_view()),
    path('product/',ProductHandler.as_view()),
]
