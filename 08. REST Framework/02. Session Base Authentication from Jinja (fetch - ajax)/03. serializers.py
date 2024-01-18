# Important part for API serialization

# https://www.django-rest-framework.org/api-guide/fields/

from rest_framework import serializers

class GenerateTextSerializer(serializers.Serializer):
    input_text = serializers.CharField(max_length=1000)
