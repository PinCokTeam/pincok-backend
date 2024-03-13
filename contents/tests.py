from django.test import TestCase

from contents.models import Contents


class ContentsCreateAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.contents = Contents.objects.create(
            title='test_title',
            detail='test_detail',
            pos_x=0,
            pos_y=0,
        )

    def test_list_contents(self):
        response = self.client.get('/contents')
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['title'], self.contents.title)
        expect_data = ['title']
        self.assertListEqual(list(response_data[0].keys()), expect_data)

    def test_inquiry_contents(self):
        response = self.client.get(f'/contents/{self.contents.id}')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 5)

    def test_create_contents(self):
        request_data = {
            'title': 'asd',
            'detail': 'test_detail',
            'pos_x': 1.1,
            'pos_y': 2.2,
        }
        response = self.client.post('/contents', data=request_data)
        self.assertEqual(response.status_code, 201)

        response_data = response.json()
        self.assertEqual(response_data['title'], request_data['title'])
        self.assertEqual(response_data['detail'], request_data['detail'])
        self.assertEqual(response_data['pos_x'], request_data['pos_x'])
        self.assertEqual(response_data['pos_y'], request_data['pos_y'])
        # self.assertEqual(response_data['member_id'], 1)
        # self.assertEqual(response_data['crew_id'], 1)

        self.assertTrue(Contents.objects.filter(id=response_data['id']).exists())

    def test_update_contents(self):
        request_data = {
            'title': 'test_title',
            'detail': 'test_detail',
            'pos_x': 3.3,
            'pos_y': 2.2,
        }
        response = self.client.put(f'/contents/{self.contents.id}', data=request_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['title'], request_data['title'])
        self.assertEqual(response_data['detail'], request_data['detail'])
        self.assertEqual(response_data['pos_x'], request_data['pos_x'])
        self.assertEqual(response_data['pos_y'], request_data['pos_y'])
        self.assertTrue(Contents.objects.filter(id=self.contents.id).exists())

    def test_delete_contents(self):
        response = self.client.delete(f'/contents/{self.contents.id}')
        self.assertEqual(response.status_code, 204)
        # sql = SELECT * FROM contents WHERE id=5000
        self.assertFalse(Contents.objects.filter(id=self.contents.id).exists())
