from django.core.exceptions import ValidationError
from .models import CustomUser, Profile
from django.test import TestCase

class ProfileModelNegativeTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='kavin', email='kavin11@gmail.com', password='kavin@12345'
        )

    def test_profile_creation_missing_required_fields(self):
        with self.assertRaises(ValueError):
            Profile.objects.create(
                user=self.user,
                mobile='',
                address='',
                pincode='',
                addresses=[]
            )

    def test_profile_creation_invalid_email(self):
        with self.assertRaises(ValidationError):
            CustomUser.objects.create_user(
                username='john', email='invalidemail', password='password123'
            )

    def test_profile_creation_invalid_mobile(self):
        with self.assertRaises(ValidationError):
            Profile.objects.create(
                user=self.user,
                mobile='invalid_mobile',
                address='123 Street',
                pincode='123456',
                addresses=['Another address']
            )

    def test_profile_update_invalid_mobile(self):
        profile = Profile.objects.create(
            user=self.user,
            mobile='9761256987',
            address='No 7, Main colony street Chennai',
            pincode='651234',
            addresses=['No 11 East colony street Chennai']
        )
        with self.assertRaises(ValidationError):
            profile.mobile = 'invalid_mobile'
            profile.full_clean()  
            profile.save()

    def test_profile_deletion_with_user(self):
        profile = Profile.objects.create(
            user=self.user,
            mobile='9761256987',
            address='No 7, Main colony street Chennai',
            pincode='651234',
            addresses=['No 11 East colony street Chennai']
        )
        self.user.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(pk=profile.pk)

    def tearDown(self):
        CustomUser.objects.filter(username='kavin').delete()
