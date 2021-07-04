from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home , name='index'),
    path('add_invoice', views.add_invoice , name='add_invoice'),
    path('list_invoice', views.list_invoice , name='list_invoice'),
    path('update_invoice/<str:pk>/', views.update_invoice, name='update_invoice'),
    path('delete_invoice/<str:pk>/', views.delete_invoice , name='delete_invoice'),
    path('link/<str:pk>/', views.Shorten_url, name='link'),
    path('pstatus/', views.webhook, name='pstatus'),
]
