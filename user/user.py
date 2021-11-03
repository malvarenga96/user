from user import hasher as hash_algorithms


class User:

    hasher: hash_algorithms.Hasher = None

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self.hasher.hash(password)

    def __str__(self):
        return f'User(username={self.username}, password={self.password})'
