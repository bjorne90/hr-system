from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or objects for the tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, about_me='About me', phone_number='123456789',
                                              address='Test Address', work_title='Test Work Title')

    def test_profile_creation(self):
        # Test the creation of a profile instance
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.about_me, 'About me')
        self.assertEqual(profile.phone_number, '123456789')
        self.assertEqual(profile.address, 'Test Address')
        self.assertEqual(profile.work_title, 'Test Work Title')

    def test_profile_str(self):
        # Test the string representation of the profile
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')

    def test_profile_default_image(self):
        # Test the default profile image
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_image.name, 'default_profile_image.png')


class ProfileSignalTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or objects for the tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_created_signal(self):
        # Test the signal that creates a profile instance when a user is created
        profile = Profile.objects.get(user=self.user)
        self.assertIsNotNone(profile)

    def test_profile_saved_signal(self):
        # Test the signal that saves the profile instance when the user is saved
        self.user.username = 'newusername'
        self.user.save()
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user.username, 'newusername')
