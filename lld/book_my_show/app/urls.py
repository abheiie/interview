from django.urls import path

from .views.customer_view import CustomerDetailView, CustomerListView

v1_urlpatterns = [
    path("api/v1/customers/", CustomerListView.as_view(), name="customer-list"),
    path("api/v1/customers/<int:id>", CustomerDetailView.as_view(), name="customer-detail")
]


urlpatterns = v1_urlpatterns
