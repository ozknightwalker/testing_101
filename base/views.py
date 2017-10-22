from __future__ import unicode_literals

import json

from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'homepage.html'
