from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType


class PetType(Model):
    nome = StringType(
        required=True, deserialize_from="name", serialized_name="name"
    )
    cor = StringType(
        required=True, deserialize_from="fur", serialized_name="fur"
    )


class Pessoa(Model):
    nome = StringType(
        required=True, deserialize_from="name", serialized_name="name"
    )
    idade = IntType(
        serialize_when_none=False,
        deserialize_from="age",
        serialized_name="age",
    )
    linguagens = ListType(
        StringType,
        serialize_when_none=False,
        deserialize_from="lang",
        serialized_name="blabla",
    )
    pets = ListType(ModelType(PetType))
