from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import generics
from .models import Wedding, Style, Provider
from .serializers import WeddingSerializer, StyleSerializer, ProviderSerializer


class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the weddings api home route!'}
    return Response(content)
  
class WeddingList(generics.ListCreateAPIView):
  queryset = Wedding.objects.all()
  serializer_class = WeddingSerializer

class WeddingDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Wedding.objects.all()
  serializer_class = WeddingSerializer
  lookup_field = 'id'

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    providers_not_associated = Provider.objects.exclude(id__in=instance.providers.all())
    providers_serializer = ProviderSerializer(providers_not_associated, many=True)

    return Response({
        'provider': serializer.data,
        'providers_not_associated': providers_serializer.data
    })

class StyleListCreate(generics.ListCreateAPIView):
  serializer_class = StyleSerializer

  def get_queryset(self):
    wedding_id = self.kwargs['wedding_id']
    return Style.objects.filter(wedding_id=wedding_id)

  def perform_create(self, serializer):
    wedding_id = self.kwargs['wedding_id']
    wedding = Wedding.objects.get(id=wedding_id)
    serializer.save(wedding=wedding)

class StyleDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = StyleSerializer
  lookup_field = 'id'

  def get_queryset(self):
    wedding_id = self.kwargs['wedding_id']
    return Style.objects.filter(wedding_id=wedding_id)
  
class ProviderList(generics.ListCreateAPIView):
  queryset = Provider.objects.all()
  serializer_class = ProviderSerializer

class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Provider.objects.all()
  serializer_class = ProviderSerializer
  lookup_field = 'id'

class AddProviderToWedding(APIView):
  def post(self, request, wedding_id, provider_id):
    wedding = Wedding.objects.get(id=wedding_id)
    provider = Provider.objects.get(id=provider_id)
    wedding.providers.add(provider)
    return Response({'message': f'Provider {provider.name} added to Wedding {wedding.description}'})
  
class RemoveProviderFromWedding(APIView):
  def post(self, request, wedding_id, provider_id):
    wedding = Wedding.objects.get(id=wedding_id)
    provider = Provider.objects.get(id=provider_id)
    wedding.providers.remove(provider)
    return Response({'message': f'Provider {provider.name} removed from Wedding {wedding.description}'})