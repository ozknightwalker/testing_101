from __future__ import unicode_literals

import factory

from base.models import Entry
from base.tests.factories.user import UserFactory


__all__ = (
    'EntryFactory',
)


class EntryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Entry

    owner = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'Test entry %s' % n)
