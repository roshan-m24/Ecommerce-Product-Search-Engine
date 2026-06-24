
from django.urls import path
from .views import SearchView
urlpatterns=[path('products/search',SearchView.as_view())]
