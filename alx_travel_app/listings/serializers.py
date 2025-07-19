from .models import Listing, Booking, User, Review
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model.
    """
    
    class Meta:
        model = Listing
        fields = ["id", 'name', 'description', 'location', 'price_per_night', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    """
    
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'start_date', 'end_date', 'status', 'created_at'] 