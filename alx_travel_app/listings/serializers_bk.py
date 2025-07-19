from rest_framework import serializers
from .models import Listing, Booking
from .models import User  # Assuming User model lives in users app


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='user_id', read_only=True)  # Expose user_id as id

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'role',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

# -------------------
# Listing Serializer
# -------------------
class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    id = serializers.UUIDField(source='listing_id', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'host',
            'name',
            'description',
            'location',
            'pricepernight',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'host', 'created_at', 'updated_at']

# -------------------
# Booking Serializer
# -------------------
class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    id = serializers.UUIDField(source='booking_id', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'user',
            'start_date',
            'end_date',
            'total_price',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'status']

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data
