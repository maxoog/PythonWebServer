from User import *


class UserBank(object):
    def __init__(self):
        self._users: [User] = []

    def __init__(self, users: [User]):
        self._users = users

    def get(self, id: int):
        if len(self._users) < id:
            raise NoSuchUserException()
        if len(self._users) == id:
            new_user = User.random_user()
            self._users.append(new_user)
            return new_user
        return self._users[id]

    def count(self):
        return len(self._users)

    def get_all(self):
        return self._users

    def change_name(self, id, name):
        if id < len(self._users):
            self._users[id].name = name
        else:
            raise NoSuchUserException()

    @staticmethod
    def empty_bank():
        return UserBank()

    @staticmethod
    def random_bank(capacity: int):
        return UserBank([User.random_user() for i in range(capacity)])
