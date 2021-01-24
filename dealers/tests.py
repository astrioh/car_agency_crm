from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Dealer, DealerType


User = get_user_model()

class DealerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='abc', password='somepassword')

        dealer_type = DealerType.objects.create(name="Юридическое лицо")
        Dealer.objects.create(name="ИП ШахМаш",
            contact="Шахов Степан",
            address="г. Ярославль",
            phone="+79159731441",
            email="shakhmash@mail.ru",
            dealer_type=dealer_type)

        cls.current_count = Dealer.objects.all().count()
        

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_dealer_created(self):
        dealer = Dealer.objects.create(name="ООО ооо",
            contact="Бабаев Роман",
            address="г. Ярославль",
            phone="+7961331441",
            email="babaev@mail.ru",
            dealer_type=DealerType.objects.get(id=1))

        self.assertEqual(dealer.id, 2)
        self.assertEqual(dealer.dealer_type, DealerType.objects.get(id=1))

        
    def test_dealer_list(self):
        client = self.get_client()
        response = client.get("/api/dealers/")
        print(response.json()['results'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
