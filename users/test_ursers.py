from django.test import TestCase
from .models import CustomUser, Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='kavin', email='kavin11@gmail.com', password='kavin@12345'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            mobile='9761256987',
            address='No 7, Main colony street Chennai',
            pincode='651234',
            addresses=['No 11 East colony street Chennai']
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'kavin')
        self.assertEqual(self.profile.mobile, '9761256987')
        self.assertEqual(self.profile.address, 'No 7, Main colony street Chennai')
        self.assertEqual(self.profile.pincode, '651234')
        self.assertEqual(self.profile.addresses, ['No 11 East colony street Chennai'])

    def test_profile_update(self):
        new_mobile = '9871267912'
        new_address = 'No 12 east colony street Karur'
        new_pincode = '651234'
        new_addresses = ['No 10 Left main road Coimbatore']

        self.profile.mobile = new_mobile
        self.profile.address = new_address
        self.profile.pincode = new_pincode
        self.profile.addresses = new_addresses
        self.profile.save()

        updated_profile = Profile.objects.get(user=self.user)

        self.assertEqual(updated_profile.mobile, new_mobile)
        self.assertEqual(updated_profile.address, new_address)
        self.assertEqual(updated_profile.pincode, new_pincode)
        self.assertEqual(updated_profile.addresses, new_addresses)

    def tearDown(self):
        CustomUser.objects.filter(username='Kavin').delete()

