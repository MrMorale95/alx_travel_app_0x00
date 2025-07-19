import random
import uuid
from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import User, Listing
from alx_travel_app.listings.models import UserRole

class Command(BaseCommand):
    help = "Seed the database with sample users and listings."

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Listing.objects.all().delete()
        User.objects.filter(role=UserRole.HOST).delete()

        self.stdout.write("Creating sample users and listings...")

        # Create sample host users
        hosts = []
        for i in range(3):
            user = User.objects.create_user(
                username=f"host{i}",
                email=f"host{i}@example.com",
                password="password123",
                first_name=f"Host{i}",
                last_name="Example",
                role=UserRole.HOST
            )
            hosts.append(user)
            self.stdout.write(f"Created host user: {user.email}")

        # Sample listing data
        sample_listings = [
            {
                "name": "Cozy Cabin in the Woods",
                "description": "A peaceful cabin retreat.",
                "location": "Yosemite, CA",
                "pricepernight": 120.00
            },
            {
                "name": "Modern Apartment in City Center",
                "description": "Close to all major attractions.",
                "location": "New York, NY",
                "pricepernight": 250.00
            },
            {
                "name": "Beachside Bungalow",
                "description": "Wake up to the sound of waves.",
                "location": "Miami, FL",
                "pricepernight": 180.00
            },
        ]

        # Create sample listings
        for data in sample_listings:
            listing = Listing.objects.create(
                host=random.choice(hosts),
                **data
            )
            self.stdout.write(f"Created listing: {listing.name}")

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully."))
