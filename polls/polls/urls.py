from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', PollsIndexView.as_view(), name='polls_list'),
    path('<int:pk>/', PollsDetailView.as_view(), name='polls_detail'),
    path('<int:pk>/vote/', vote, name='vote'),
]
