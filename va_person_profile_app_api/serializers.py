from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    photo = serializers.FileField(use_url=False, required=False)

    class Meta:
        model = Profile
        fields = ('__all__')