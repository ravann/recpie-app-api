from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = "test@test.com"
        passwd = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=passwd
        )
        print("User is : " + str(user))
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(passwd))

    def test_create_user_with_nickname(self):
        """Create user with nickname"""
        email = "test@test.com"
        passwd = "test1234"
        nickname = "Nick"
        user = get_user_model().objects.create_user(
            email=email,
            password=passwd,
            nickname=nickname
        )
        print("Nickname is : %s" % user.nickname)
        self.assertEqual(user.nickname, nickname)

    def test_user_email_normalized(self):
        """Check if the users email is normalized"""
        email = "test@tesT.com"
        passwd = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=passwd
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_no_email(self):
        """Test if the User Manager throws exception if an user is
        created with blank email."""
        with self.assertRaises(ValueError):
            email = None
            passwd = "test1234"
            get_user_model().objects.create_user(
                email=email,
                password=passwd
            )

    def test_create_new_superuser(self):
        """Test creating a super user"""
        email = "test@tesT.com"
        passwd = "test1234"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=passwd
        )
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
