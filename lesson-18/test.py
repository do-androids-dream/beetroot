import re


class EmailHolder:
    VALID_PREFIX_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9]+(?:[_.-][a-zA-Z0-9]+)*$")
    VALID_DOMAIN_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9-]+(\.[a-zA-Z0-9]{2,})$")
    AT_SYMBOL = "@"

    def __init__(self, email: str):
        if self.validate(email.strip()):
            self.email = email.strip()
        else:
            raise ValueError(f"Invalid email: {email}")

    @classmethod
    def validate(cls, email: str) -> bool:
        if cls.AT_SYMBOL not in email:
            return False

        prefix, domain = email.split("@")

        is_valid_prefix = bool(cls.VALID_PREFIX_EMAIL_PATTERN.fullmatch(prefix))
        is_valid_domain = bool(cls.VALID_DOMAIN_EMAIL_PATTERN.fullmatch(domain))

        return is_valid_prefix and is_valid_domain