from django.test import Client, TestCase
from django.urls import resolve, reverse
from profiles.models import Profile, User
from pytest_django.asserts import assertTemplateUsed
import pytest


class TestLettingApp(TestCase):
    client = Client()

    @pytest.mark.django_db
    def setUp(self):
        user = User.objects.create(
            username="Test",
            password="test",
            first_name="user",
            last_name="tested",
            email="usertested@email.com"
        )
        Profile.objects.create(
            user=user,
            favorite_city="Issou"
        )

    @pytest.mark.django_db
    def test_profiles_index_view(self):
        path = reverse('profiles:profiles_index')
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert Profile.objects.all().first().user.username in content
        assertTemplateUsed(response, 'profiles/index.html')

    @pytest.mark.django_db
    def test_profile_detail_view(self):
        profile = Profile.objects.all().first()
        path = reverse('profiles:profile', kwargs={'username': profile.user.username})
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert profile.favorite_city in content
        assertTemplateUsed(response, 'profiles/profile.html')

    def test_profiles_index_url(self):
        path = reverse('profiles:profiles_index')
        assert path == '/profiles/'
        assert resolve(path).view_name == 'profiles:profiles_index'

    @pytest.mark.django_db
    def test_profile_detail_url(self):
        profile = Profile.objects.all().first()
        path = reverse('profiles:profile', kwargs={'username': profile.user.username})
        assert path == '/profiles/Test/'
        assert resolve(path).view_name == 'profiles:profile'

    @pytest.mark.django_db
    def test_user_model(self):
        user = User.objects.get(username="Test")
        expected_value = "Test"
        assert str(user.username) == expected_value

    @pytest.mark.django_db
    def test_profile_model(self):
        profile = Profile.objects.get(favorite_city="Issou")
        expected_value = "Test"
        assert str(profile) == expected_value
