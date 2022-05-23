from utils import *


class NoSuchUserException(Exception):
    pass


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @staticmethod
    @count_calls
    def random_user():
        _id: int = User.next_id()
        return User(id=_id, name=chr(ord('A') - 1 + _id) * 8)

    @staticmethod
    def next_id() -> int:
        return User.random_user.calls
