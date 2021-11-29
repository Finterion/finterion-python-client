from abc import abstractmethod


class Model:

    @staticmethod
    @abstractmethod
    def from_dict(data):
        pass
