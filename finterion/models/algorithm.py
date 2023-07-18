from finterion.models.model import Model


class Algorithm(Model):

    def __init__(
        self,
        id,
        name,
        title,
        environment,
    ):
        self.id = id
        self.name = name
        self.title = title
        self.environment = environment

    @staticmethod
    def from_dict(data):
        return Algorithm(
            id=data.get("id"),
            name=data.get("name"),
            title=data.get("title"),
            environment=data.get("environment"),
        )

    def to_dict(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "title": self.get_title(),
            "environment": self.get_environment(),
        }

    def __repr__(self):
        return self.repr(
            id=self.id,
            name=self.name,
            title=self.title
        )

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def get_environment(self):
        return self.environment
