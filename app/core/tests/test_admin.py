from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        email = "admin@test.com"
        passwd = "test1234"
        self.admin_user = get_user_model().objects.create_superuser(
            email=email, password=passwd)
        self.client.force_login(self.admin_user)
        uemail = "user@test.com"
        self.user = get_user_model().objects.create_user(
            email=uemail, password=passwd)

    def test_users_listed(self):
        """Test user are listed on user page"""
        url = reverse('admin:core_custuser_changelist')
        print("URL is : %s" % url)

        res = self.client.get(url)

        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test the user edit page works"""
        url = reverse('admin:core_custuser_change', args=[self.user.id])
        print("Change URL: %s" % url)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works"""
        url = reverse('admin:core_custuser_add')
        print('ADD User URL: %s' % url)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
