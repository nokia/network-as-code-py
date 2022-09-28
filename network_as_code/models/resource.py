from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ..api import APIClient


class Model:
    """A base class for representing a single resource instance."""

    def __init__(self, attrs: dict, api: "APIClient", collection: "Collection"):
        # The remote API which fulfils requests.
        self.api = api

        # The collection that this model is part of.
        self.collection = collection

        # The raw representation of this object from the API.
        self.attrs = {} if attrs is None else attrs

    # TODO: Add __repr__ method.
    # TODO: Add __eq__ method.

    @property
    def id(self) -> str:
        """The ID of the object."""
        return self.attrs.get("sid", "")

    def reload(self):
        """
        Load this object from the API and update `attrs` with the new data.
        """
        _model = self.collection.get(self.id)
        self.attrs = _model.attrs


class Collection:
    """A base class for representing all available resources of a particular type."""

    # The type of object this collection represents, set by subclasses.
    model = None

    def __init__(self, api: "APIClient"):
        # The API client that has access to this object.
        self.api = api

    def list(self):
        raise NotImplementedError  # Implemented by subclass

    def get(self, id: str):
        raise NotImplementedError  # Implemented by subclass

    def create(self, attrs=None):
        raise NotImplementedError  # Implemented by subclass

    def prepare_model(self, attrs: "Model|dict"):
        """Create a model from a set of attributes."""
        if self.__class__ is Collection:
            raise Exception("This method should not be called from the base class")

        if self.model is None:
            raise Exception("Subclass forgot to define the 'model' attribute")

        if isinstance(attrs, Model):
            attrs.api = self.api
            attrs.collection = self
            return attrs

        if isinstance(attrs, dict) and issubclass(self.model, Model):
            return self.model(attrs=attrs, api=self.api, collection=self)

        if isinstance(self.model, Model):
            raise Exception(f"Can't create a {self.model.__name__} from {attrs}")
        else:
            raise Exception(
                f"Subclass {self.__class__.__name__} did not specify the model attribute"
            )
