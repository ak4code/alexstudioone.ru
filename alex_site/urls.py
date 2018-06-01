from django.urls import path
from .views import Home, PageDetail, PartyList, PartyDetail, FeedView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('page/<slug:slug>/', PageDetail.as_view(), name='page'),
    path('party/', PartyList.as_view(), name='party-list'),
    path('party/<slug:slug>/', PartyDetail.as_view(), name='party-detail'),
    path('feedback/', FeedView.as_view(), name='feedback'),
]
