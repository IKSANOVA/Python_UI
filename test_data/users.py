import random

_users = [
    ("test2@mail.ru", "test"),
    ("test3@mail.ru", "test"),
    ("test4@mail.ru", "test"),
]


def get_user():
    return random.choice(_users)
