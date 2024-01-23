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

#########################################################


from typing import Callable


class TypeDecorators:

    def __getattribute__(self, item):
        types = {
            "bool": bool,
            "int": int,
            "float": float,
            "str": str,
        }

        if item.startswith("to_"):
            parts = item.split("_")
            if len(parts) == 2:
                type_ = parts[1]
                if type_ in types:
                    return self._to_type(types[type_])

        return super().__getattribute__(item)

    def _to_type(self, type_: Callable):
        ...  # <----- Your decorator here


@TypeDecorators().to_str
def test():
    return 17


if __name__ == "__main__":
    test()
