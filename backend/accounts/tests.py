from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):
    def test_eigenes_benutzermodell_ist_aktiv(self):
        self.assertEqual(get_user_model()._meta.label, 'accounts.User')

    def test_benutzer_anlegen_speichert_passwort_als_hash(self):
        user = get_user_model().objects.create_user(username='test', password='Geheim123!')
        self.assertNotEqual(user.password, 'Geheim123!')
        self.assertTrue(user.check_password('Geheim123!'))


class AdminTests(TestCase):
    def test_admin_login_seite_erreichbar(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_admin_ohne_login_leitet_weiter(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
