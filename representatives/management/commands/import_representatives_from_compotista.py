# coding: utf-8

# This file is part of compotista.
#
# compotista is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# compotista is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>



from django.core.management.base import BaseCommand
from django.conf import settings

from urllib2 import urlopen
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from representatives.utils import import_representatives


class Command(BaseCommand):
    def handle(self, *args, **options):
        compotista_server = getattr(settings,
                                    'REPRESENTATIVES_COMPOTISTA_SERVER',
                                    'http://compotista.mm.staz.be')
        url = compotista_server + "/latest/"
        print('Import representatives from %s' % url)
        stream = BytesIO(urlopen(url))
        import_representatives(JSONParser().parse(stream))