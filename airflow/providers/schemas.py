from marshmallow import Schema, fields, EXCLUDE

# [
# 	{
# 		"flights": [
# 			{
# 				"duration": 5700,
# 				"segments": [
# 					{
# 						"operating_airline": "DV",
# 						"marketing_airline": "DV",
# 						"flight_number": "703",
# 						"equipment": null,
# 						"dep": {
# 							"at": "2021-11-12T05:40:00+06:00",
# 							"airport": "ALA"
# 						},
# 						"arr": {
# 							"at": "2021-11-12T07:15:00+06:00",
# 							"airport": "NQZ"
# 						},
# 						"baggage": "0PC"
# 					}
# 				]
# 			},
# 			{
# 				"duration": 5700,
# 				"segments": [
# 					{
# 						"operating_airline": "DV",
# 						"marketing_airline": "DV",
# 						"flight_number": "704",
# 						"equipment": null,
# 						"dep": {
# 							"at": "2021-11-13T08:15:00+06:00",
# 							"airport": "NQZ"
# 						},
# 						"arr": {
# 							"at": "2021-11-13T09:50:00+06:00",
# 							"airport": "ALA"
# 						},
# 						"baggage": "0PC"
# 					}
# 				]
# 			}
# 		],
# 		"refundable": false,
# 		"validating_airline": "DV",
# 		"pricing": {
# 			"total": "19253.00",
# 			"base": "12000.00",
# 			"taxes": "7253.00",
# 			"currency": "KZT"
# 		}
# 	},
# ]


# class FlightSchema(Schema):
#     class Meta:
#         unknown = EXCLUDE
#
#     duration = fields.Integer()
#     segments = fields.Nested()
# 				"segments": [
# 					{
# 						"operating_airline": "DV",
# 						"marketing_airline": "DV",
# 						"flight_number": "703",
# 						"equipment": null,
# 						"dep": {
# 							"at": "2021-11-12T05:40:00+06:00",
# 							"airport": "ALA"
# 						},
# 						"arr": {
# 							"at": "2021-11-12T07:15:00+06:00",
# 							"airport": "NQZ"
# 						},
# 						"baggage": "0PC"
# 					}
# 				]

#
# class ProviderAInSchema(Schema):
#     class Meta:
#         unknown = EXCLUDE
#
#     flights = fields.Nested(FlightSchema(), many=True)
#     refundable = fields
#     validating_airl = fieldsine
#     pricing = fields
