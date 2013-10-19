import logging
from mediagoblin.tools import pluginapi
import os

# log information to the console or a log file.
_log = logging.getLogger(__name__)

PLUGIN_DIR = os.path.dirname(__file__)

def setup_plugin():
    config = pluginapi.get_config('advanced-sampleplugin')
    if config:
        _log.info('%r' % config)
    else:
        _log.info('There is no configuration set.')

    pluginapi.register_template_path(os.path.join(PLUGIN_DIR, 'templates'))

    pluginapi.register_template_hooks(
        {"persona_end": "advanced-sampleplugin/template.html"})


hooks = {
    'setup': setup_plugin
    }
