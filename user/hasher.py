import abc
import hashlib


class Hasher(abc.ABC):
    @abc.abstractmethod
    def hash(self, password):
        pass


class SHA256Hasher(Hasher):
    def hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Blake2Hasher(Hasher):
    def hash(self, password):
        return hashlib.blake2b(password.encode()).hexdigest()
