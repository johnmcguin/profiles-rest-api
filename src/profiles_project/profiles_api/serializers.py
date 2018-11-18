from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
    
# model serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile objects."""

    # tells django rest framework what fields we want from model
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # password should be write only
        # extra key word args
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        # encrypts passphrase
        user.set_password(validated_data['password'])
        user.save()
        return user