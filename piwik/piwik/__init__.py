# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from mediagoblin.tools import pluginapi
import os

_log = logging.getLogger(__name__)

PLUGIN_DIR = os.path.dirname(__file__)

def setup_plugin():
    global config 
    config = pluginapi.get_config('piwik')

    if config:
        _log.info('%r' % config)
    else:
        _log.info('There is no configuration set.')

    pluginapi.register_template_path(os.path.join(PLUGIN_DIR, 'templates'))

    pluginapi.register_template_hooks(
        {"persona_end": "mediagoblin/piwik/template.html"})

def add_to_global_context(context):
    context['piwik'] = config
    return context

hooks = {
    'setup': setup_plugin,
    'template_global_context': add_to_global_context
    }
