from django.test import TestCase
from .models import Bus, User, Book

class BusModelTest(TestCase):
    def setUp(self):
        Bus.objects.create(bus_name='Bus1', source='Location1', dest='Location2', nos=10, rem=5, price=100.00, date='2022-01-01', time='10:00:00')

    def test_bus_name(self):
        bus = Bus.objects.get(id=1)
        expected_object_name = f'{bus.bus_name}'
        self.assertEquals(expected_object_name, 'Bus1')

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(user_id=1, email='test@test.com', name='Test User', password='testpassword')

    def test_user_email(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.email}'
        self.assertEquals(expected_object_name, 'test@test.com')

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(email='test@test.com', name='Test User', userid=1, busid=1, bus_name='Bus1', source='Location1', dest='Location2', nos=1, price=100.00, date='2022-01-01', time='10:00:00', status='B')

    def test_book_email(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.email}'
        self.assertEquals(expected_object_name, 'test@test.com')