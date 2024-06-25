from src.models.abstract_model import AbstractModel
from src.database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }
