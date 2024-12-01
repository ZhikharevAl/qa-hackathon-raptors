from typing import ClassVar

from faker import Faker

fake = Faker()


class Payloads:
    """Payloads for users."""

    create_user: ClassVar[dict[str, str]] = {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
        "nickname": fake.user_name(),
    }
