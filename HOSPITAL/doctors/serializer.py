from rest_framework.serializers import ModelSerializer
from.models import junnu
class junnuSerializer(ModelSerializer):
    class Meta:
        model=junnu
        fields="__all__"