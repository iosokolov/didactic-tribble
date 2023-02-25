from uuid import UUID

from marshmallow import Schema, fields


class SearchOutSchema(Schema):
    search_id = fields.UUID()
