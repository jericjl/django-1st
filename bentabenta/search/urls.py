from django.urls import path
from .views import SearchProductView

app_name = 'search'
urlpatterns =[
    path('search/',SearchProductView.as_view(),name='query'),
]