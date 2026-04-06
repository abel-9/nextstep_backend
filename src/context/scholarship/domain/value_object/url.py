from urllib.parse import urlparse

from src.context.shared_kernel.domain.value_objects.value_object import ValueObject


class Url(ValueObject[str]):
    def __init__(self, value: str):
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Invalid URL. Expected an absolute http(s) URL.")
        super().__init__(value=value)
