from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ First Test"""
        email = 'test@example.com'
        password = 'User1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email_succesfull(self):
        """Second Test"""
        sample_email = [('Abcd@Gmail.com', 'abcd@gmail.com'),
                        ('abc@Exampl.Com', 'abc@exampl.com'),
                        ('xyz@EXAMPLE.com', 'xyz@example.com'),
                        ('XYZK@EXAMPLE.COM', 'xyzk@example.com')
                        ]
        password = 'ABCD1234'
        for email, expected_email in sample_email:
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )
            self.assertEqual(user.email, expected_email)

    def test_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'password')

    def test_with_create_superuser(self):
        user = get_user_model().objects.create_superuser(email='asd@gmail.com', password='pass12345')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)