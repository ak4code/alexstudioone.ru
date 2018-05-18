from django.urls import path
from .views import Home, PageDetail, PartyList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('page/<slug:slug>/', PageDetail.as_view(), name='page'),
    path('party', PartyList.as_view(), name='party-list')
]
