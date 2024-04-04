from django.urls import path
from .views import Home, WeddingList, WeddingDetail, StyleListCreate, StyleDetail, ProviderList, ProviderDetail, AddProviderToWedding, RemoveProviderFromWedding

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('weddings/', WeddingList.as_view(), name='wedding-list'),
  path('weddings/<int:id>/', WeddingDetail.as_view(), name='wedding-detail'),
  path('weddings/<int:wedding_id>/styles/', StyleListCreate.as_view(), name='style-list-create'),
	path('weddings/<int:wedding_id>/styles/<int:id>/', StyleDetail.as_view(), name='style-detail'),
  path('providers/', ProviderList.as_view(), name='provider-list'),
  path('providers/<int:id>/', ProviderDetail.as_view(), name='provider-detail'),
  path('weddings/<int:wedding_id>/add_provider/<int:provider_id>/', AddProviderToWedding.as_view(), name='add-provider-to-wedding'),
  path('weddings/<int:wedding_id>/remove_provider/<int:provider_id>/', RemoveProviderFromWedding.as_view(), name='remove-provider-from-wedding'), 
]
