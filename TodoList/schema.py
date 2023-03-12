import graphene
from graphene_django import DjangoObjectType
from authors.models import Book, Author


class BookType(DjangoObjectType):  # objects of model book
    class Meta:  # special type for books
        model = Book  # - list of objects of model book
        fields = '__all__'


class AuthorType(DjangoObjectType):  # objects of model book
    class Meta:  # special type for books
        model = Author  # - list of objects of model book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))

    def resolve_all_books(self, info):  # what will re returned (filters)
        return Book.objects.all()

    def resolve_all_authors(self, info):  # what will re returned (filters)
        return Author.objects.all()

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name):
        books = Book.objects.all()
        if name:
            books = books.filter(author__first_name=name)
        return books


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, route, info, birthday_year, id):
        author = Author.objects.get(pk=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)  # here we connect query and resolver to our scheme
