from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String(default_value='stranger'))
    goodbye = String()

    def resolve_hello(self, info, name):
        return f'Hello {name}'

    def resolve_goobye(self, info):
        return "See You"


schema = Schema(query=Query)
print(schema)
