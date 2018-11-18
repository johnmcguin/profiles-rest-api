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


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # only want current logged in user to be able to add their own posts for that user
        extra_kwargs = {'user_profile': {'read_only': True}}