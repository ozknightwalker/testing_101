from __future__ import unicode_literals

import factory

from base.models import Profile
from base.tests.factories.user import UserFactory


__all__ = (
    'ProfileFactory',
)


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    owner = factory.SubFactory(UserFactory)
    full_name = factory.LazyAttribute(
        lambda profile: '{0} {1}'.format(
            profile.owner.first_name, profile.owner.last_name))
