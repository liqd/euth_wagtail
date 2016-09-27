import factory
from tests.factories import UserFactory


class FakeProjectContent(factory.django.DjangoModelFactory):
    class Meta:
        model = 'fakeprojects.FakeProjectContent'

    creator = factory.SubFactory(UserFactory)
