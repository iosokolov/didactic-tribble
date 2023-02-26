from uuid import UUID

from marshmallow import Schema, fields

from constants import StatusEnum


class SearchOutSchema(Schema):
    search_id = fields.UUID()


class ItemSchema(Schema):
    a = fields.Boolean()


class ResultOutSchema(Schema):
    search_id = fields.UUID()
    status = fields.Enum(StatusEnum)
    items = fields.List(fields.Nested(ItemSchema()))
