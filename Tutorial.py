import json, graphene, os


# class Query(graphene.ObjectType):
#     name = graphene.String()
#     age  = graphene.String()
    
    
#     ##reolve_nameofargument
#     def resolve_name(root, info ):
#         return "Akshat"
#     def resolve_age(root, info):
#         return "23"
    
    
# schema = graphene.Schema(query=Query)
# print(schema)


# ##QUERY

# query1 = """
# query myquery{
#     myname : name
#     myage: age
# }

# """

# result = schema.execute(query1)
# print(result)
# print(json.dumps(result.data, indent=4))


################################ ARGUMENTS #####################################

# class Query(graphene.ObjectType):
#     name = graphene.String(customName = graphene.String(default_value = "Akshat") )
#     age  = graphene.String()
    
    
#     ##reolve_nameofargument
#     def resolve_name(root, info, customName ):
#         return customName
#     def resolve_age(root, info):
#         return "23"
    
    
# schema = graphene.Schema(query=Query)
# print(schema)


# ##QUERY

# query1 = """
# query myquery{
#     myname : name (customName:"Akshay")
#     myage: age
# }

# """

# result = schema.execute(query1)
# print(result)
# print(json.dumps(result.data, indent=4))





############## DIFF TYPES OF SCALAR

# DATA = [
#     {
#         "name":"Akshat",
#         "age":"23"
#     },
#     {
#         "name":"Akshay",
#         "age":"22"
#     }
# ]


# class Person(graphene.ObjectType):
#     name = graphene.String()
#     age = graphene.String()


# class Query(graphene.ObjectType):
    
#     array = graphene.List(Person, size = graphene.Int(default_value=1))
    
#     def resolve_array(root, info, size):
#         return DATA[:size]
    
# schema = graphene.Schema(query=Query, auto_camelcase=False)
# print(schema)
# print("\n--------------------------------------------\n")
# ##QUERY
# query1 = """
# query myquery {
#     array (size:2) {
#     personsName: name    personsAge: age
#     }
# }
# """
# result = schema.execute(query1)
# print(result)
# print(json.dumps(result.data, indent=4))


################################################ MUTATIONS #################


# DATA = [
#     {
#         "name":"Akshat",
#         "age":"23"
#     },
#     {
#         "name":"Akshay",
#         "age":"22"
#     }
# ]

# class Person(graphene.ObjectType):
#     name = graphene.String()
#     age = graphene.String()

# class CreatePerson(graphene.Mutation):
#     class Arguments:
#         personname = graphene.String()
#         personage = graphene.String(default_value="21")
    
#     ok = graphene.Boolean()
#     person = graphene.Field(Person)
    
#     def mutate(self, info, personname, personage):
#         person = Person(name = personname, age = personage)
#         ok = True
#         return CreatePerson(person = person, ok = ok)
        
# class MyMutation(graphene.ObjectType):
#     createPerson = CreatePerson.Field()
    

# class Query(graphene.ObjectType):
#     person = graphene.Field(Person)
    
# schema = graphene.Schema(query=Query,mutation=MyMutation, auto_camelcase=False)
# print(schema)
# print("\n--------------------------------------------\n")


# query1 = """
# mutation myFirstMutation {
#     createPerson(personname: "Peter", personage: "25"){
#         person{
#             personName:name
#             age
#         }
#         ok
#     }
# }
# """
# result = schema.execute(query1)
# print(result)
# print(json.dumps(result.data, indent=4))





################################## INPUT FIELDS #####################
class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()
    
class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.String(default_value = "22")

class CreatePerson(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)
    
    ok = graphene.Boolean()
    person = graphene.Field(Person)
    
    def mutate(self, info, person_data):
        person = Person(name = person_data.name, age = person_data.age)
        ok = True
        return CreatePerson(person = person, ok = ok)
        
class MyMutation(graphene.ObjectType):
    createPerson = CreatePerson.Field()
    

class Query(graphene.ObjectType):
    person = graphene.Field(Person)
    
schema = graphene.Schema(query=Query,mutation=MyMutation)
print(schema)
print("\n--------------------------------------------\n")


query1 = """
mutation myFirstMutation {
    createPerson(personData:{name: "Peter"}){
        person{
            personName:name
            age
        }
        ok
    }
}
"""
result = schema.execute(query1)
print(result)
print(json.dumps(result.data, indent=4))

