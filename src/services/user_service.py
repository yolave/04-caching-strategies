import time
from typing import List

from ..adapters.memory_db import MemoryUserRepository
from ..models.user import UserIn, UserOut
from ..ports.db_port import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user: UserIn) -> UserOut:
        # Simulate a delay to mimic a real database operation
        time.sleep(8)
        return self.repo.create(user)

    def list_users(self) -> List[UserOut]:
        # Simulate a delay to mimic a real database operation
        time.sleep(8)
        return self.repo.list()


user_service = UserService(MemoryUserRepository())


def get_user_service() -> UserService:
    return user_service
