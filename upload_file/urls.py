from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("treat_data/", views.treat_data, name="treat_data"),
    path("transactions/", views.transactions, name="transactions"),
    path("api/transactions/", views.TransactionView.as_view(), name="api_transactions"),
]