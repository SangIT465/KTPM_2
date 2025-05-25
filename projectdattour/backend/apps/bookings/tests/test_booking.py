from django.test import TestCase
from django.urls import reverse
from ..models import Booking
from django.contrib.auth import get_user_model
from apps.tours.models import Tour, TourCategory, Destination, TourDate
from datetime import date

class TestBookingCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Tạo các đối tượng liên quan
        category = TourCategory.objects.create(name='Trong nước', slug='trong-nuoc')
        destination = Destination.objects.create(name='Đà Lạt', slug='da-lat')
        self.tour = Tour.objects.create(
            category=category,
            destination=destination,
            title='Tour Đà Lạt',
            slug='tour-da-lat',
            short_description='Du lịch Đà Lạt',
            description='Du lịch Đà Lạt',
            duration=3,
            price=1000000,
            main_image='image.jpg',
            itinerary='Lịch trình',
            includes='Bao gồm',
            excludes='Không bao gồm',
            terms='Điều khoản'
        )
        # Thêm đoạn này để tạo tour_date
        self.tour_date = TourDate.objects.create(
            tour=self.tour,
            start_date=date.today(),
            end_date=date.today(),
            tour_price=1000000,
            available_seats=10,
            is_active=True
        )
        self.client.login(username='testuser', password='testpass')

    def test_create_booking(self):
        response = self.client.post(reverse('bookings:booking-create'), {
            'tour': self.tour.id,
            'user': self.user.id,
            'quantity': 2,
            'adults': 2,
            'children': 0,
            'tour_date': self.tour_date.id,
        })
        print(response.context['form'].errors)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user, tour=self.tour).exists())