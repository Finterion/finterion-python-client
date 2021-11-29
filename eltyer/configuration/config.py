import os
from eltyer.configuration.constants import BASE_URL, ORDERS_ENDPOINT


class Config(dict):
    LOG_LEVEL = 'INFO'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    api_key = None
    host = BASE_URL

    def __init__(self):
        super().__init__()

        for attribute_key in dir(Config):

            if attribute_key.isupper():
                self[attribute_key] = getattr(self, attribute_key)

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __str__(self):
        field_strings = []

        for attribute_key in self:

            if attribute_key.isupper():
                field_strings.append(
                    f'{attribute_key}='
                    f'{self[attribute_key]!r}'
                )

        return f"<{self.__class__.__name__}({','.join(field_strings)})>"

    def get(self, key: str, default=None):
        """
        Mimics the dict get() functionality
        """

        try:
            return self[key]
        # Ignore exception
        except Exception:
            pass

        return default

    def set(self, key: str, value) -> None:
        self[key] = value

    @staticmethod
    def from_dict(dictionary):
        config = Config()

        for attribute_key in dictionary:

            if attribute_key:
                config.set(attribute_key, dictionary[attribute_key])
                config[attribute_key] = dictionary[attribute_key]
        return config
