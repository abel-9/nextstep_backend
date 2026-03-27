import argon2
from argon2.exceptions import VerifyMismatchError


class Argon2Hasher:
    """Argon2id implementation (Memory-hard, GPU-resistant)."""

    def __init__(self):
        self._ph = argon2.PasswordHasher()

    def hash(self, password: str) -> str:
        return self._ph.hash(password)

    def verify(self, hashed: str, password: str) -> bool:
        try:
            return self._ph.verify(hashed, password)
        except (VerifyMismatchError, Exception):
            return False

    def needs_rehash(self, hashed: str) -> bool:
        return self._ph.check_needs_rehash(hashed)
