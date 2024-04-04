from rest_framework import serializers
from .models import Wedding, Style, Provider

class ProviderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Provider
    fields = '__all__'
    
class WeddingSerializer(serializers.ModelSerializer):
  providers = ProviderSerializer(many=True, read_only=True) #add this line
  class Meta:
    model = Wedding
    fields = '__all__'

class StyleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Style
    fields = '__all__'
    read_only_fields = ('style',)

