from rest_framework import serializers
from .models import Category, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

        # converts languages
        def to_representation(self, instance):
            # Determine language from request or context and serialize accordingly
            request = self.context.get('request')
            if request and request.LANGUAGE_CODE == 'pl':
                instance.name = instance.name_pl
                instance.description = instance.description_pl
            return super().to_representation(instance)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

        # converts languages
        def to_representation(self, instance):
            # Determine language from request or context and serialize accordingly
            request = self.context.get('request')
            if request and request.LANGUAGE_CODE == 'pl':
                instance.name = instance.name_pl
                instance.description = instance.description_pl
            return super().to_representation(instance)