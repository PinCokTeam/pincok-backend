from django.test import TestCase
from rest_framework.test import APIClient
from member.models import Member


# Create your tests here.
class MemberAPI_테스트(TestCase):
    client_class: APIClient = APIClient

    @classmethod
    def setUpTestData(cls):
        cls.member = Member.objects.create(
            name="name"
        )

    def test_멤버_목록조회요청(self):
        response = self.client.get('/member')
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['name'], self.member.name)

    def test_멤버_상세조회요청(self):
        response = self.client.get(f'/member/{self.member.id}')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], response_data['name'])
        self.assertTrue(Member.objects.filter(id=self.member.id).exists())

    def test_멤버_생성(self):
        response = self.client.post('/member', data={
            'name': 'name'
        })
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['name'], response_data['name'])
        self.assertTrue(Member.objects.filter(id=self.member.id).exists())

    def test_멤버_수정요청(self):
        request_data = {
            'name': 'sub'
        }
        response = self.client.put(f'/member/{self.member.id}', data=request_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], response_data['name'])
        self.assertTrue(Member.objects.filter(id=self.member.id).exists())

    def test_멤버_삭제요청(self):
        response = self.client.delete(f'/member/{self.member.id}')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Member.objects.filter(id=self.member.id).exists())
