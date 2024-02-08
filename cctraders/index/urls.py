from django.urls import path
from .views import index_view, farmer_view, logistics_view, waste_management_view

urlpatterns = [
    path('index.html', index_view, name='index'),
    path('farmer-page.html', farmer_view, name='farmer-page'),
    path('logistics-page.html', logistics_view, name='logistics-page'),
    path('waste-management.html', waste_management_view, name='waste-management'),
    # path('contact/', ContactFormView.as_view(), name='contact-form'),
]