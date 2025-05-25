from django.test import TestCase
from django.urls import reverse
from ..models import Tour, TourCategory, Destination

class TestTourSearchCase(TestCase):
    def setUp(self):
        category = TourCategory.objects.create(name='Trong nước', slug='trong-nuoc')
        destination = Destination.objects.create(name='Đà Nẵng', slug='da-nang')
        Tour.objects.create(
            category=category,
            destination=destination,
            title='Tour Đà Nẵng',
            slug='tour-da-nang',
            short_description='Du lịch Đà Nẵng',
            description='Du lịch Đà Nẵng',
            duration=3,
            price=1000000,
            main_image='image.jpg',
            itinerary='Lịch trình',
            includes='Bao gồm',
            excludes='Không bao gồm',
            terms='Điều khoản'
        )
        destination2 = Destination.objects.create(name='Hà Nội', slug='ha-noi')
        Tour.objects.create(
            category=category,
            destination=destination2,
            title='Tour Hà Nội',
            slug='tour-ha-noi',
            short_description='Du lịch Hà Nội',
            description='Du lịch Hà Nội',
            duration=3,
            price=1000000,
            main_image='image.jpg',
            itinerary='Lịch trình',
            includes='Bao gồm',
            excludes='Không bao gồm',
            terms='Điều khoản'
        )

    def test_search_tour_by_name(self):
        response = self.client.get(reverse('tours:tour-search'), {'q': 'Đà Nẵng'})
        self.assertContains(response, 'Tour Đà Nẵng')
        self.assertNotContains(response, 'Tour Hà Nội')