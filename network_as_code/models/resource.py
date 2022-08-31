from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ..client import NetworkAsCodeClient


class Model:
    """A base class for representing a single object."""

    def __init__(
        self,
        attrs: dict = None,
        client: "NetworkAsCodeClient" = None,
        collection=None,
    ):
        # The client that has access to this object.
        self.client = client

        # The collection that this model is part of.
        self.collection = collection

        # The raw representation of this object from the API.
        self.attrs = {} if attrs is None else attrs

    # TODO: Add __repr__ method.
    # TODO: Add __eq__ method.

    @property
    def id(self):
        """The ID of the object."""
        return self.attrs.get("id")

    def reload(self):
        """
        Load this object from the API and update `attrs` with the new data.
        """
        _model = self.collection.get(self.id)
        self.attrs = _model.attrs


class Collection:
    """A base class for representing all objects of a particular type."""

    # The type of object this collection represents, set by subclasses.
    model = None

    def __init__(self, client: "NetworkAsCodeClient" = None):
        # The client that has access to this object.
        self.client = client

    def list(self):
        raise NotImplementedError  # Implemented by subclass

    def get(self, id: str):
        raise NotImplementedError  # Implemented by subclass

    def create(self, attrs=None):
        raise NotImplementedError  # Implemented by subclass

    def prepare_model(self, attrs: "Model|dict"):
        """Create a model from a set of attributes."""
        if isinstance(attrs, Model):
            attrs.client = self.client
            attrs.collection = self
            return attrs

        elif isinstance(attrs, dict):
            return self.model(attrs=attrs, client=self.client, collection=self)

        else:
            raise Exception(f"Can't create {self.model.__name__} from {attrs}")
