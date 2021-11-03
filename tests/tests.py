import hashlib
from unittest import TestCase
from unittest.mock import patch

from user import hasher, User


class UserTest(TestCase):
    def setUp(self):
        self.username = 'test_username'
        self.password = 'test_password'

    @patch('user.User.hasher', new=hasher.SHA256Hasher())
    def test_sha256_hasher(self):
        hash = hashlib.sha256(self.password.encode()).hexdigest()

        user = User(self.username, self.password)
        self.assertEqual(user.password, hash)

    @patch('user.User.hasher', new=hasher.Blake2Hasher())
    def test_blake2_hasher(self):
        hash = hashlib.blake2b(self.password.encode()).hexdigest()

        user = User(self.username, self.password)
        self.assertEqual(user.password, hash)
