from .models import Contacts

class UserSerializer(serializers.ModelSerializer):
    # serialize groups with "slugs" ↓
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field='Whos_Phone'
     )
