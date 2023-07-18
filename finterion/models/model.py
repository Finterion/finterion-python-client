from abc import abstractmethod


class Model:

    @staticmethod
    @abstractmethod
    def from_dict(data):
        pass

    def repr(self, **fields) -> str:
        """
        Helper for __repr__
        """

        field_strings = []

        for key, field in fields.items():
            field_strings.append(f'{key}={field!r}')

        return f"<{self.__class__.__name__}({','.join(field_strings)})>"
