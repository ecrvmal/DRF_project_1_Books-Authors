import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from authors.views import AuthorModelViewSet
from authors.models import Author, Biography


# Create your tests here.


class TestAuthorViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.data = {'first_name': 'Aleksandr', 'last_name': 'Pushkin', "birthday_year": 1799, }
        self.data_put = {'first_name': 'Nikolay', 'last_name': 'Gumilev', "birthday_year": 1901, }

        self.url = '/api/authors'
        self.admin = User.objects.create_superuser(username=self.name,
                                                   password=self.password,
                                                   email=self.email)

    # testing API VIEW AuthorModelViewSet
    def test_get_list(self):
        factory = APIRequestFactory()  # создали объект
        request = factory.get(self.url)  # создали тип запроса factory направляем запрос
        view = AuthorModelViewSet.as_view({'get': 'list'})  # as_view  - from url   б передаем методы туда
        #  не отправляем реальный запрос на сервер, а эмултруем похожий запрос,
        # и передаем его в API VIEW
        #     view = AuthorModelViewSet.as_view({'post': 'create'})
        #     view = AuthorModelViewSet.as_view({'delete': 'destroy'})
        #     view = AuthorModelViewSet.as_view({'update': 'post'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #        Authorization test
    def test_create_guest(self):
        factory = APIRequestFactory()  # создали объект
        request = factory.post(self.url, self.data, format='json')  # создали тип запроса factory направляе
        view = AuthorModelViewSet.as_view({'post': 'create'})  # as_view  - from url   б передаем методы туда
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):  # test with admin rights: create author
        factory = APIRequestFactory()  # создали объект
        request = factory.post(self.url, self.data, format='json')  # создали тип запроса factory направляе
        force_authenticate(request, self.admin)  # user authorization
        view = AuthorModelViewSet.as_view({'post': 'create'})  # as_view  - from url   б передаем методы туда
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        author = Author.objects.create(**self.data)
        # print('\n author', author)
        # print(f'{self.url}/{author.id}/')
        response = client.get(f'{self.url}/{author.id}/')
        # print('response', response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest_api(self):
        client = APIClient()  # права не нужны, запускаем с API консоли
        author = Author.objects.create(**self.data)
        response = client.put(f'{self.url}/{author.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin_api(self):
        client = APIClient()  # права не нужны, запускаем с API консоли
        author = Author.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}/{author.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        auth = Author.objects.get(id=author.id)
        self.assertEqual(auth.first_name, 'Nikolay')
        self.assertEqual(auth.last_name, 'Gumilev')
        self.assertEqual(auth.birthday_year, 1901)
        client.logout()

    def tearDown(self) -> None:
        pass


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        response = math.sqrt(4)
        self.assertEqual(response, 2)


class TestBiographyViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'
        self.data_author = {'first_name': 'Aleksandr', 'last_name': 'Pushkin', "birthday_year": 1799, }
        self.author = Author.objects.create(**self.data_author)
        self.data = {'text': 'Text_Create', 'author': self.author}
        self.data_put = {'text': 'Text_Update', 'author': self.author}

        self.url = '/api/biography/'
        self.admin = User.objects.create_superuser(username=self.name,
                                                   password=self.password,
                                                   email=self.email)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        bio = Biography.objects.create(**self.data)
        self.client.login(username=self.name, password=self.password)  # authorization as admin
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Text_Update', 'author': bio.author.id})  # or  'author': bio.author_id
        # response = self.client.put(f'{self.url}{bio.id}/', self.data_put)          this doesn't work
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio_ = Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text, 'Text_Update')
        self.client.logout()

    def test_put_mixer(self):
        bio = mixer.blend(Biography)  # mixer will create the object with all params with links
        self.client.login(username=self.name, password=self.password)  # authorization as admin
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Text_Update', 'author': bio.author.id})  # or  'author': bio.author_id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bio_ = Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text, 'Text_Update')
        self.client.logout()

    def test_put_mixer_field(self):
        bio = mixer.blend(Biography, text='My_Biography')  # mixer will create the object with all params with links
        self.assertEqual(bio.text, 'My_Biography')
        self.client.login(username=self.name, password=self.password)  # authorization as admin
        response = self.client.put(f'{self.url}{bio.id}/',
                                   {'text': 'Text_Update', 'author': bio.author.id})  # or  'author': bio.author_id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bio_ = Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text, 'Text_Update')
        self.client.logout()

    def tearDown(self) -> None:
        pass
