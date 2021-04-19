from graphene import ObjectType, String, Float, Boolean, List

class Currency(ObjectType):
    id = String()
    name = String()
    color = String()
    gradients = List(String)
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()
