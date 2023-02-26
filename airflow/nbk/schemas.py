from marshmallow import Schema, fields, EXCLUDE


# 	<date>26.02.2023</date>
# 	<item>
# 		<fullname>АВСТРАЛИЙСКИЙ ДОЛЛАР</fullname>
# 		<title>AUD</title>
# 		<description>303.7</description>
# 		<quant>1</quant>
# 		<index></index>
# 		<change>0.00</change>
# 	</item>

class ItemInSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    fullname = fields.String()
    title = fields.String()
    description = fields.Decimal()
    quant = fields.Decimal()


class RateInSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    date = fields.Date(format='%d.%m.%Y')
    items = fields.List(fields.Nested(ItemInSchema()))
