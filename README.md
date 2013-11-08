# Readme

This is a loose collection of various plugins I write/wrote
for the [GNU MediaGoblin](http://mediagoblin.org) project.

A while ago I dumped flickr and deviantart and migrated to
my own [MediaGoblin instance](http://media.micha.elmueller.net). 
I have been sitting silently on the developers list since then. 
I guess it's finally time to start developing :).

**Project status:** I am just starting out writing stuff for
MediaGoblin. Some things may still be a little bit wobbly.


# Plugins

## advanced-sampleplugin

An advanced version of the 
[sampleplugin](http://mediagoblin.readthedocs.org/en/latest/pluginwriter/quickstart.html)
described in the MediaGoblin documentation. This one uses template hooks,
template variables, config files and default configuration.

## piwik

Piwik is a the free software alternative to Google Analytics.
This (very simple plugin) inserts your Piwik tracking code right before 
`</body>`. Sure you could also just add the code in the theme directly. 
But then you would have to add it after each MediaGoblin update. Using 
a plugin is more comfortable.

## flattr

Adds a [Flattr](http://flattr.com/) auto-submit button to each media entry 
detail view.


# Helpful links

[http://mediagoblin.readthedocs.org/en/v0.5.1/pluginwriter/api.html](MediaGoblin Plugin API)


# License

MediaGoblin is licensed under AGPLv3, thus the plugins have to be as well.
See `LICENSE` for the AGPLv3 text.
