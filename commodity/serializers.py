from rest_framework import serializers
from .models import Bag

class BagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'