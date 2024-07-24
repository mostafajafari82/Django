from rest_framework import serializers
from commodity.models import Bag
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'#["name", "family", "age"]


class BagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'